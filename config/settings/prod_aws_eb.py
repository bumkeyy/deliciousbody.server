from .common_aws import *
import os

ALLOWED_HOSTS= ['*']
DEBUG = False

WSGI_APPLICATION = 'config.wsgi.prod_aws_eb.application'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'HOST': os.environ['DB_HOST'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'NAME': os.environ['DB_NAME'],
        'PORT': os.environ['DB_PORT'],
    },
}

INSTALLED_APPS += ['storages',]

STATICFILES_STORAGE = 'deliciousbody_api_server.storages.StaticS3Boto3Storage'
DEFAULT_FILE_STORAGE = 'deliciousbody_api_server.storages.MediaS3Boto3Storage'

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', 'ap-northeast-2')

AWS_DEFAULT_ACL = None