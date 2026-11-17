#!/usr/bin/env bash
# Ежедневный снимок media (фото диванов, страниц и отзывов).
#
#   ~/backups/kama_website/media/media_2026-11-17/   полная копия каталога media на эту дату
#
# Снимки инкрементальные: rsync --link-dest делает жёсткие ссылки на неизменившиеся файлы
# предыдущего снимка. Первый снимок занимает размер media, каждый следующий — только новые
# и изменённые файлы. При этом каждый снимок можно восстановить целиком сам по себе.
# Резервный сервер забирает их через rsync -aH, и там они тоже не раздуваются.
#
# Не шифруется: всё в media и так публично отдаётся сайтом, а шифрование убило бы инкрементальность.
set -euo pipefail
umask 077

SRC="$HOME/kama_website/media"
OUT_DIR="$HOME/backups/kama_website/media"
KEEP=5            # сколько последних снимков хранить
MIN_RATIO=80      # если файлов стало меньше 80% от прошлого снимка — не снимаем, это похоже на аварию
RESERVE_MB=500    # после снимка на диске должно остаться не меньше

mkdir -p "$OUT_DIR"

today="media_$(date +%F)"
dest="$OUT_DIR/$today"
tmp="$OUT_DIR/.$today.tmp"

if [ -d "$dest" ]; then
  echo "$(date '+%F %T') SKIP: $today уже есть"
  exit 0
fi

[ -d "$SRC" ] || { echo "$(date '+%F %T') ERROR: нет каталога $SRC" >&2; exit 1; }

prev=$(find "$OUT_DIR" -mindepth 1 -maxdepth 1 -type d -name 'media_????-??-??' | sort | tail -n1)

# Защита от того, чтобы пустой или наполовину удалённый media не вытеснил ротацией хорошие снимки.
src_n=$(find "$SRC" -type f | wc -l)
if [ -n "$prev" ]; then
  prev_n=$(find "$prev" -type f | wc -l)
  if [ $(( src_n * 100 )) -lt $(( prev_n * MIN_RATIO )) ]; then
    echo "$(date '+%F %T') ERROR: в media $src_n файлов, в прошлом снимке $prev_n. Снимок не сделан" >&2
    exit 1
  fi
fi

# Диск на сервере почти заполнен: без снимка лучше, чем с переполненным диском и упавшей БД.
# Первый снимок — полная копия, следующие — только изменения (оцениваем сверху размером media).
need_mb=$RESERVE_MB
[ -n "$prev" ] || need_mb=$(( $(du -sm "$SRC" | cut -f1) + RESERVE_MB ))
free_mb=$(df -Pm "$OUT_DIR" | awk 'NR==2 {print $4}')
if [ "$free_mb" -lt "$need_mb" ]; then
  echo "$(date '+%F %T') ERROR: свободно ${free_mb} МБ, нужно ${need_mb} МБ. Снимок не сделан" >&2
  exit 1
fi

# Без -o/-g/-p: файлы принадлежат пользователю cron, иначе --link-dest не сможет ставить ссылки.
# Если прошлый запуск упал, rsync докачает в тот же .tmp.
rsync -rlt --delete ${prev:+--link-dest="$prev"} "$SRC/" "$tmp/"
mv "$tmp" "$dest"

# Ротация по количеству, а не по дате: если снимки перестанут делаться, старые не исчезнут.
find "$OUT_DIR" -mindepth 1 -maxdepth 1 -type d -name 'media_????-??-??' | sort | head -n -"$KEEP" \
  | while read -r d; do rm -rf "$d"; done
# Остатки упавших запусков за прошлые дни
find "$OUT_DIR" -mindepth 1 -maxdepth 1 -type d -name '.media_*.tmp' ! -name ".$today.tmp" -exec rm -rf {} +

total=$(du -sh "$OUT_DIR" | cut -f1)   # du считает жёсткие ссылки один раз, это реальный объём
echo "$(date '+%F %T') OK $today, файлов: $src_n, всего снимков: $(find "$OUT_DIR" -mindepth 1 -maxdepth 1 -type d -name 'media_*' | wc -l), занято: $total"
