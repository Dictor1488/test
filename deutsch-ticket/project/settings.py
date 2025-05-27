import os
from pathlib import Path

# BASE_DIR указывает на корень проекта (где manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'ваш-секретный-ключ')

DEBUG = False  # в продакшене всегда False

# Добавляем ваш Railway-домен (или список доменов) чтобы убрать DisallowedHost
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'test-production-e61f.up.railway.app',  # ваш Railway URL
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'tickets',  # ← ваше приложение
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # подключаем WhiteNoise сразу после SecurityMiddleware
    'whitenoise.middleware.WhiteNoiseMiddleware',  

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # шаблоны берем из apps
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# База данных — для начала пусть будет простая SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    # ... дефолтные валидаторы
]

LANGUAGE_CODE = 'de-de'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_TZ = True


# Статика (css, js, лого)
STATIC_URL = '/static/'
# В продакшене отдаем через WhiteNoise

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'tickets' / 'static',
]


# Медиа (загружаемые фото и QR)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
