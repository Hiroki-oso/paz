from pathlib import Path
import os
import environ
env = environ.Env()
from django.contrib import messages 

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')




# ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# 開発環境
DEBUG = True
env.read_env(os.path.join(BASE_DIR,'.env'))
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS=['*']

# 本番環境
# デプロイ設定
# DEBUG = False

# try:
#     from .local_settings import *
# except ImportError:
#     pass

# ローカル用設定
# if DEBUG = True:
#    ALLOWED_HOSTS = ['*']
#    env.read_env(os.path.join(BASE_DIR,'.env'))
#    SECRET_KEY = env('SECRET_KEY')

# if not DEBUG:
#     import environ
#     env = environ.Env()
#     env.read_env(os.path.join(BASE_DIR,'.env'))
#     SECRET_KEY = env('SECRET_KEY')

#   STATIC_ROOT = '/usr/share/nginx/html/static'


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts.apps.AccountsConfig",
    "myapp.apps.MyappConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR,],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ja"
TIME_ZONE = "Asia/Tokyo"
USE_I18N = True
USE_TZ = True

AUTH_USER_MODEL = 'accounts.User'

STATIC_URL = "static/"
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# ログイン、ログアウト
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/list/'
LOGOUT_URL = '/logout/'
LOGOUT_REDIRECT_URL = '/'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'alert alert-danger',
    messages.WARNING: 'alert alert-warning',
    messages.INFO: 'alert alert-info',
    messages.SUCCESS: 'alert alert-success',
}
