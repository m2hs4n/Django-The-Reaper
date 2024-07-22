#!/bin/sh

# Exit immediately
set -e

# Run makemigrations
python manage.py makemigrations

# Run migrate
python manage.py migrate

# Start the Django server
exec "$@"
