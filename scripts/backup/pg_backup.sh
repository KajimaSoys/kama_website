#!/usr/bin/env bash
# Ежечасный зашифрованный дамп БД из контейнера db-kama.
#
#   ~/backups/kama_website/db/hourly/db_2026-11-17_1435.dump.age   каждый час, хранится KEEP_HOURLY штук
#   ~/backups/kama_website/db/daily/db_2026-11-17.dump.age         первый удачный дамп за сутки, KEEP_DAILY штук
#
# Формат pg_dump -Fc (сжатый, восстанавливается через pg_restore).
# Шифрование age по открытому ключу: сервер может зашифровать, но не расшифровать.
# pg_dump запускается внутри контейнера через локальный сокет (trust), пароль не нужен.
#
# Восстановление (на машине с приватным ключом):
#   age -d -i key.txt db_....dump.age > db.dump
#   docker exec -i db-kama pg_restore -U "$DB_USER" -d "$DB_NAME" --clean --if-exists --no-owner < db.dump
set -euo pipefail
umask 077

CONTAINER="db-kama"
OUT_DIR="$HOME/backups/kama_website/db"
KEEP_HOURLY=48    # двое суток почасовых
KEEP_DAILY=30     # месяц ежедневных
MIN_SIZE=10240    # дамп меньше 10 КБ считаем битым: в базе есть данные
AGE_RECIPIENTS="$(dirname "$(readlink -f "$0")")/age-recipients.txt"   # список открытых ключей

[ -s "$AGE_RECIPIENTS" ] || { echo "$(date '+%F %T') ERROR: нет $AGE_RECIPIENTS" >&2; exit 1; }

mkdir -p "$OUT_DIR/hourly" "$OUT_DIR/daily"

name="db_$(date +%F_%H%M).dump.age"
tmp="$OUT_DIR/hourly/.$name.tmp"
trap 'rm -f "$tmp"' EXIT

# pipefail: если pg_dump упадёт, упадёт и весь конвейер, и .tmp не станет бэкапом.
docker exec "$CONTAINER" sh -c 'exec pg_dump -U "$POSTGRES_USER" -d "$POSTGRES_DB" -Fc' \
  | age -R "$AGE_RECIPIENTS" -o "$tmp"

size=$(stat -c %s "$tmp")
if [ "$size" -lt "$MIN_SIZE" ]; then
  echo "$(date '+%F %T') ERROR: дамп подозрительно маленький ($size байт), не сохраняю" >&2
  exit 1
fi
mv "$tmp" "$OUT_DIR/hourly/$name"

# Первый дамп за сутки становится ежедневным. Жёсткая ссылка: места не занимает.
daily="$OUT_DIR/daily/db_$(date +%F).dump.age"
[ -e "$daily" ] || ln "$OUT_DIR/hourly/$name" "$daily"

# Ротация по количеству, а не по дате: если дампы перестанут делаться, старые не исчезнут.
rotate() {  # rotate <каталог> <шаблон> <сколько оставить>
  find "$1" -maxdepth 1 -type f -name "$2" | sort | head -n -"$3" | while read -r f; do rm -f "$f"; done
}
rotate "$OUT_DIR/hourly" 'db_????-??-??_????.dump.age' "$KEEP_HOURLY"
rotate "$OUT_DIR/daily"  'db_????-??-??.dump.age'      "$KEEP_DAILY"
find "$OUT_DIR" -name '.*.tmp' -mmin +120 -delete

echo "$(date '+%F %T') OK $name ($(du -h "$OUT_DIR/hourly/$name" | cut -f1)), всего: $(du -sh "$OUT_DIR" | cut -f1)"
