release: python manage.py collectstatic
web: gunicorn Project.wsgi  --preload --workers 1