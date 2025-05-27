import os
from django.core.wsgi import get_wsgi_application

# Убедитесь, что здесь указано именно имя вашего проекта —
# если вы запускали: django-admin startproject project .
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_wsgi_application()
