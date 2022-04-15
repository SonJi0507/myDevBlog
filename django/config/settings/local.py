from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

CORS_ORIGIN_WHITELIST = get_secret("CORS_ORIGIN_WHITELIST")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}