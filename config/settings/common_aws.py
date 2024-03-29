import os, json, datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(BASE_DIR)

SECRET_KEY = os.environ['secret_key']
SERVER_KEY = os.environ['fcm_server_key']
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
    #"rest_framework_swagger",

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
    'accounts', # custom user

    # logging
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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Email login 및 username 비활성화, email 검증 비활성
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_UNIQUE_USERNAME = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False

# email 인증
ACCOUNT_EMAIL_VERIFICATION = 'none'

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
EMAIL_HOST = os.environ['smtp_host']
EMAIL_HOST_USER = os.environ['smtp_host_user']
EMAIL_HOST_PASSWORD = os.environ['smtp_host_password']
EMAIL_PORT = os.environ['smtp_port']
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_QUERY_EMAIL = True

REST_AUTH_SERIALIZERS = {
    'PASSWORD_RESET_SERIALIZER':
        'userinfo.serializers.PasswordResetSerializer',
    #'USER_DETAILS_SERIALIZER':
    #    'accounts.serializers.MyUserDetailSerializer',
    #'REGISTER_SERIALIZER':
    #    'accounts.serializers.MyRegisterSerializer',
}
REST_AUTH_REGISTER_SERIALIZERS = {
        'REGISTER_SERIALIZER': 'accounts.serializers.MyRegisterSerializer',
}

ACCOUNT_LOGOUT_ON_GET = True