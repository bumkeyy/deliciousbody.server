"""
Django settings for deliciousbody_api_server project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os, json, datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(BASE_DIR)

CONFIG_SECRET_DIR = os.path.join(BASE_DIR, '.config_secret')
CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')
CONFIG_SECRET_DEBUG_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_debug.json')
CONFIG_SECRET_DEPLOY_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_deploy.json')
CONFIG_SECRET_AWS_DEPLOY_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_eb_deploy.json')

config_secret_common = json.loads(open(CONFIG_SECRET_COMMON_FILE).read())


SECRET_KEY = config_secret_common['django']['secret_key']
SERVER_KEY = config_secret_common['fcm']['server_key']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # drf
    "rest_framework",
    "rest_framework.authtoken",

    # doc
    "rest_framework_swagger",

    # rest-auth
    "rest_auth",

    # registration
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',

    #jwt
    'rest_framework_jwt',

    # kakao login
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',

    # fcm
    #'fcm_django',

    # app
    'userinfo',
    'video',
    'recommend_list',
    'video_list',
    'version',

    # logging
    #'raven.contrib.django.raven_compat',

]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'deliciousbody_api_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = config_secret_common['static']['url']
STATIC_ROOT = config_secret_common['static']['root']


MEDIA_URL = config_secret_common['media']['url']
MEDIA_ROOT = config_secret_common['media']['root']


# Email login 및 username 비활성화, email 검증 비활성
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_UNIQUE_USERNAME = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False

# email 인증
#ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

OLD_PASSWORD_FIELD_ENABLED = True

AUTHENTICATION_BACKENDS = (
   "django.contrib.auth.backends.ModelBackend",
   "allauth.account.auth_backends.AuthenticationBackend"
)


# Token 인증 사용
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework.authentication.BasicAuthentication',
        #'rest_framework.authentication.SessionAuthentication',
        #'rest_framework.authentication.TokenAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    )
}

JWT_AUTH = {
    'JWT_ALLOW_REFRESH' : True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=365),
}

REST_USE_JWT = True

# smtp 설정
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config_secret_common['email']['host']
EMAIL_HOST_USER = config_secret_common['email']['host_user']
EMAIL_HOST_PASSWORD = config_secret_common['email']['host_password']
EMAIL_PORT = config_secret_common['email']['port']
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_QUERY_EMAIL = True

REST_AUTH_SERIALIZERS = {
    'PASSWORD_RESET_SERIALIZER':
        'userinfo.serializers.PasswordResetSerializer',
}

ACCOUNT_LOGOUT_ON_GET = True