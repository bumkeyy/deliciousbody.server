from .base import *
import os

config_secret_deploy = json.loads(open(CONFIG_SECRET_AWS_DEPLOY_FILE).read())

DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'config.wsgi.prod_aws_eb.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config_secret_deploy['database']['name'],
        'USER': config_secret_deploy['database']['user'],
        'PASSWORD': config_secret_deploy['database']['password'],
        'HOST': config_secret_deploy['database']['host'],
        'PORT': config_secret_deploy['database']['port'],
    },
}

INSTALLED_APPS += ['storages',] # django-storages 앱 의존성 추가
# 기본 static/media 저장소를 django-storages로 변경
STATICFILES_STORAGE = 'deliciousbody_api_server.storages.StaticS3Boto3Storage'
DEFAULT_FILE_STORAGE = 'deliciousbody_api_server.storages.MediaS3Boto3Storage'
# S3 파일관리에필요한최소설정
# 소스코드에 설정정보를 남기지마세요. 환경변수를 통한 설정 추천
AWS_ACCESS_KEY_ID = config_secret_deploy['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config_secret_deploy['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config_secret_deploy['aws']['storage_bucket_name']
# 필수 지정 # 필수 지정 # 필수 지정
AWS_S3_REGION_NAME = config_secret_deploy['aws']['s3_region_name']

AWS_DEFAULT_ACL = None