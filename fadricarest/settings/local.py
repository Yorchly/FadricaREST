from fadricarest.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fadricarest',
        'USER': 'admin',
        'PASSWORD': os.environ.get("FADRICAREST_DATABASE_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '',
    }
}
