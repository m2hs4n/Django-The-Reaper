#!/bin/sh


# Run makemigrations
python manage.py makemigrations

# Run migrate
python manage.py migrate

# Run test
python manage.py test