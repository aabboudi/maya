"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

SETTINGS_MODULE = 'core.prod_settings' if 'WEBSITE_HOSTNAME' in os.environ else 'core.dev_settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_MODULE)

application = get_wsgi_application()
