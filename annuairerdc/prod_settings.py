import dj_database_url
from .settings import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


TEMPLATES_DEBUG = False


ALLOWED_HOSTS = ['rdcannuaire.herokuapp.com']

DATABASES['default'] = dj_database_url.config()

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
