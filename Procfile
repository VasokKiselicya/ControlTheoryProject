release: python manage.py collectstatic --noinput
release: python manage.py compilemessages
web: gunicorn Project.wsgi  --preload --workers 1