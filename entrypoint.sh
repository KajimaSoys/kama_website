#!/bin/sh
set -eu

# makemigrations на сервере не запускаем: миграции создаются локально и коммитятся в репозиторий.
python manage.py migrate --noinput
python manage.py collectstatic --noinput --verbosity 0

exec "$@"
