import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']
SECRET_KEY = 'django-insecure-^w0+)&&ycaex5gk3ub9t7u+&bc826^c-jm7$0+w8842wr7$cuc'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",# from nginx in prod
    "http://localhost:5173",# from vite in dev
    "http://localhost:4173"
]

CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']

CORS_ALLOW_HEADERS = ['accept', 'accept-encoding', 'authorization', 'content-type', 'dnt', 'origin', 'user-agent', 'x-csrftoken', 'x-requested-with', 'Access-Control-Allow-Origin']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kama',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': 'D:/Programming/rezal_prom_website/cache'
#     }
# }

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.mail.ru'
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
# EMAIL_HOST_USER = 'rezal.mebel@mail.ru'
# EMAIL_HOST_PASSWORD = 'PDkMgqV1WHPC7D1GH50Q'

