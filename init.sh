#!/bin/sh
export PGPASSWORD='alumnodb'
#A rellenar: escribir alumnodb siempre
dropdb -U alumnodb exam
createdb -U alumnodb exam

python manage.py makemigrations application
python manage.py migrate

python manage.py createsuperuser

python populate.py
