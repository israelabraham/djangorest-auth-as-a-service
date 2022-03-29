"""
WSGI config for djangorest_auth project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from djangorest_auth.config.base import RUNTIME_ENVIRON
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", RUNTIME_ENVIRON)

application = get_wsgi_application()
