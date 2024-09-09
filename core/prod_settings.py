import os
from .dev_settings import *

DEBUG = False

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]

CSRF_TRUSTED_ORIGINS = [
    'http://'+os.environ['WEBSITE_HOSTNAME'],
    'https://'+os.environ['WEBSITE_HOSTNAME'],
]

SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
