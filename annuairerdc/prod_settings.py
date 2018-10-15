import dj_database_url

from annuairerdc.settings import *


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

TEMPLATES_DEBUG = False

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['rdcannuaire.herokuapp.com']

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
