from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'config.wsgi.debug.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config_secret_debug['database']['name'],
        'USER': config_secret_debug['database']['user'],
        'PASSWORD': config_secret_debug['database']['password'],
        'HOST': config_secret_debug['database']['host'],
        'PORT': config_secret_debug['database']['port'],
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''