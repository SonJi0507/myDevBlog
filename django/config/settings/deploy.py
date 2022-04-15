from .base import *

DEBUG = False
ALLOWED_HOSTS = [] #배포시 debug = false 하고 호스팅도메인,서브도메인 서비스하는 주소 적어줘야함.
                    #settings 개발용, 운영용으로 나눠서 관리할 것

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret("DEPLOY_DB_NAME"),# database name
        'USER': get_secret("DEPLOY_DB_USER"),# db user
        'PASSWORD': get_secret("DEPLOY_DB_PASSWORD"),
        'HOST': get_secret("DEPLOY_DB_HOST"),
        'PORT': get_secret("DEPLOY_DB_PORT"),
    }
}