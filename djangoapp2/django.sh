#!/usr/bin/env bash
# These will be the steps for the migrations. In other languages we have ORMs
echo 'Create Migrations'
python manage.py makemigrations djangoapp2
echo '==================================='

echo 'Migrate'
python manage.py migrate
echo '==================================='

echo 'Start server'
python manage.py runserver 0.0.0.0:8000