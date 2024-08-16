import os
from .dev_settings import *

DEBUG = False

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]

CSRF_TRUSTED_ORIGINS = [
    'http://'+os.environ['WEBSITE_HOSTNAME'],
    'https://'+os.environ['WEBSITE_HOSTNAME'],
]

# SECURE_HSTS_SECONDS = 0  # 1 year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = False
# SECURE_HSTS_PRELOAD = False
# SECURE_SSL_REDIRECT = False
# SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SECURE = False

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
