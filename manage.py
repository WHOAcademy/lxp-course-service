#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys

from lxp_course_service.preps import set_default_env


def main():
    set_default_env()

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
    main()
