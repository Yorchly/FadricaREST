import dj_database_url
import django_heroku

from fadricarest.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ["fadricarest.herokuapp.com"]

DATABASES = {
    "default": dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# Email SMTP sendgrid configuration
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.environ.get("SENDGRID_API_KEY")
# Port 465 if a HTTPS connection is used
# It's recommended in unencrypted connection use the port 587 "to avoid any rate limiting
# that your server host may apply."
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Mailing with errors to ADMINS
SERVER_EMAIL = DEFAULT_FROM_EMAIL
ADMINS = [("Jorge", os.environ.get("ADMIN_EMAIL"))]

# Secure options and Forcing Https connection
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Activate Django-Heroku.
django_heroku.settings(locals())