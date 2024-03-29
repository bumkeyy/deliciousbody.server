from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config_secret_deploy['database']['name'],
        'USER': config_secret_deploy['database']['user'],
        'PASSWORD': config_secret_deploy['database']['password'],
        'HOST': config_secret_deploy['database']['host'],
        'PORT': config_secret_deploy['database']['port'],
    }
}