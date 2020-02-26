#!/bin/bash
python manage.py makemigrations
python manage.py migrate
echo "Running seeder"
# python manage.py loaddata dockerize/seeder/estado.json
python manage.py loaddata dockerize/seeder/municipio.json
# python manage.py loaddata dockerize/seeder/localidad.json
python manage.py loaddata dockerize/seeder/organismo.json
python manage.py loaddata dockerize/seeder/sector.json
python manage.py loaddata dockerize/seeder/user.json
# python manage.py loaddata dockerize/seeder/persona.json
echo "Seeder completed"
python manage.py runserver 0.0.0.0:8000
python manage.py collectstatic