release: python manage.py collectstatic --noinput
web: gunicorn Project.wsgi  --preload --workers 1