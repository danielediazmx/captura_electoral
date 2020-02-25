#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata dockerize/estado.json
python manage.py loaddata dockerize/municipio.json
python manage.py loaddata dockerize/localidad.json
python manage.py loaddata dockerize/organismo.json
python manage.py loaddata dockerize/seccion.json
python manage.py loaddata dockerize/sector.json
python manage.py loaddata dockerize/persona.json
python manage.py runserver 0.0.0.0:8000
python manage.py collectstatic