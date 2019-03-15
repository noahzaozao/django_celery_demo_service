from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

from django.conf import settings

app = Celery('demo')

app.config_from_object('django.conf.settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
