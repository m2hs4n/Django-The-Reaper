#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


if __name__ == "__main__":
    # Determine if '--develop' or '--production' flags are provided
    develop = '--develop' in sys.argv
    production = '--production' in sys.argv

    # Set the appropriate settings module based on the provided flag
    if develop:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.develop")
        sys.argv.remove('--develop')
    elif production:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
        sys.argv.remove('--production')
    else:
        # Default to development settings if neither option is provided
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

    try:
        # Run Django's command-line utility
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)