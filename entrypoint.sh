#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

exec gunicorn kama_website.wsgi:application --bind 0.0.0.0:8000