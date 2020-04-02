#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

    from django.core.management import execute_from_command_line

    # We shouldn't be hardcoding paths like this
    # Need to refactor and consider using tools like https://dynaconf.rtfd.io

    # This does nothing, needs fixing
    # os.environ.setdefault("ENV_PATH", ".envs/.dev.env")

    execute_from_command_line(sys.argv)
