#!/usr/bin/env bash
# Ежедневный зашифрованный бэкап конфигурации:
#   .env, client/.env.production, crontab пользователя,
#   /etc/nginx, /etc/letsencrypt, /etc/docker/daemon.json (через sudo-хелпер kama-config-snapshot).
# Шифрование age по открытому ключу: сервер может зашифровать, но не расшифровать.
set -euo pipefail
umask 077

PROJECT="$HOME/kama_website"
OUT_DIR="$HOME/backups/kama_website/config"
KEEP_DAYS=30
AGE_RECIPIENTS="$(dirname "$(readlink -f "$0")")/age-recipients.txt"   # список открытых ключей

ENV_FILES=("$PROJECT/.env" "$PROJECT/client/.env.production")

[ -s "$AGE_RECIPIENTS" ] || { echo "$(date '+%F %T') ERROR: нет $AGE_RECIPIENTS" >&2; exit 1; }

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
mkdir -p "$work/project" "$OUT_DIR"

for f in "${ENV_FILES[@]}"; do
  if [ -f "$f" ]; then
    rel="${f#"$PROJECT"/}"
    mkdir -p "$work/project/$(dirname "$rel")"
    cp -p "$f" "$work/project/$rel"
  else
    echo "$(date '+%F %T') WARN: нет файла $f"
  fi
done

crontab -l > "$work/crontab.txt" 2>/dev/null || true

# Ключи letsencrypt и .htpasswd читаются только root'ом, поэтому системная часть идёт через
# фиксированный root-скрипт, которому sudoers разрешает запуск без пароля.
sudo -n /usr/local/sbin/kama-config-snapshot > "$work/system-etc.tar.gz"

name="config_$(date +%F).tar.gz.age"
tar -czf - -C "$work" . | age -R "$AGE_RECIPIENTS" -o "$OUT_DIR/$name.tmp"
mv "$OUT_DIR/$name.tmp" "$OUT_DIR/$name"

find "$OUT_DIR" -name 'config_*.tar.gz.age' -mtime +"$KEEP_DAYS" -delete
find "$OUT_DIR" -name '*.tmp' -mmin +120 -delete
echo "$(date '+%F %T') OK $name ($(du -h "$OUT_DIR/$name" | cut -f1))"
