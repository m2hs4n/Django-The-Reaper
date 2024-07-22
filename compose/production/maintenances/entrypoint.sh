#!/bin/sh

# Exit immediately
set -e

# python manage.py collectstatic

# Run makemigrations
python manage.py makemigrations

# Run migrate
python manage.py migrate

# Start the Django server
exec "$@"
