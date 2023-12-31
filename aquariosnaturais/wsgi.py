"""
WSGI config for aquariosnaturais project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aquariosnaturais.settings')

application = get_wsgi_application()
#VERCEL#app = application
application = Cling(get_wsgi_application())
