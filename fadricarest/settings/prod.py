import dj_database_url
import django_heroku

from fadricarest.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ["fadricarest.herokuapp.com"]

# For collecting statics assets and serving them
STATICFILES_STORAGE = 'common.storage.WhiteNoiseStaticFilesStorage'

DATABASES = {
    "default": dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# Secure options and Forcing Https connection
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Activate Django-Heroku.
django_heroku.settings(locals())