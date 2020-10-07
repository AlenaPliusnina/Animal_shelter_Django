release: python manage.py migrate
release: python manage.py loaddata fixtures.json
web: gunicorn my_sitegit.wsgi