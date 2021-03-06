#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from nationaldays.scraper.scraper import national_days_for_month, start_database
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nationaldaycalendar.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # start_database()
    # national_days_for_month('February')
    main()
