from email.utils import formataddr

from .base import *  # noqa: F403

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.0/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "database_cache",
    }
}

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# https://docs.djangoproject.com/en/5.0/ref/settings/#email-host
EMAIL_HOST = "maildev"
# https://docs.djangoproject.com/en/5.0/ref/settings/#email-port
EMAIL_PORT = 1025

DEFAULT_FROM_EMAIL = "Do Not Reply <do_not_reply@{{cookiecutter.domain_name}}>"

ADMINS.append(("Admin", "admin@{{cookiecutter.domain_name}}"))  # noqa: F405
LIST_OF_EMAIL_RECIPIENTS += list(map(lambda recipient: formataddr(recipient), ADMINS))  # noqa F405

# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa F405

# LOGGING
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.0/ref/settings/#logging
# See https://docs.djangoproject.com/en/5.0/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"verbose": {"format": "%(levelname)s %(asctime)s %(module)s " "%(process)d %(thread)d %(message)s"}},
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

# Django Debug Toolbar
# ------------------------------------------------------------------------------
# https://github.com/jazzband/django-debug-toolbar
INSTALLED_APPS.append("debug_toolbar")  # noqa: F405  # https://github.com/jazzband/django-debug-toolbar

# Additional middleware introduced by debug toolbar
# insert after first element value.

# The order of MIDDLEWARE and MIDDLEWARE_CLASSES is important.
# You should include the Debug Toolbar middleware as early as possible in the list.
# However, it must come after any other middleware that encodes the response's content,
# such as GZipMiddleware.
MIDDLEWARE.insert(1, "debug_toolbar.middleware.DebugToolbarMiddleware")  # noqa: F405

INTERNAL_IPS = ["127.0.0.1", "::1"]

DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: DEBUG}  # noqa: F405
