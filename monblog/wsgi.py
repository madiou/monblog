# monblog/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monblog.settings')
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monblog.wsgi.application')

application = get_wsgi_application()
