import os

from django.core.wsgi import get_wsgi_application
#from raven.contrib.django.raven_compat.middleware.wsgi import Sentry

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deliciousbody_api_server.settings")
#application = Sentry(get_wsgi_application())

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.deploy")

application = get_wsgi_application()