# django_celery_demo_service

### PreRequirements

- pyenv installed
- python 3.6.7

### Install Dependent Packages

```
pyenv activate env_celery_demo
pip install --no-cache-dir -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```

### Run celery

```
python manage.py celery worker -l info
python manage.py celery beat -l info
```

### Run django

```
python manage.py runserver 0.0.0.0:8000
```

