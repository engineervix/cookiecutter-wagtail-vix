from .base import *

# Django Debug Toolbar
INSTALLED_APPS.append(
    "debug_toolbar"
)  # https://github.com/jazzband/django-debug-toolbar

# Additional middleware introduced by debug toolbar
# insert after first element value.

# The order of MIDDLEWARE and MIDDLEWARE_CLASSES is important.
# You should include the Debug Toolbar middleware as early as possible in the list.
# However, it must come after any other middleware that encodes the response's content,
# such as GZipMiddleware.
MIDDLEWARE.insert(1, "debug_toolbar.middleware.DebugToolbarMiddleware")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ["127.0.0.1", "::1"]

# LOGGING
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

LIST_OF_EMAIL_RECIPIENTS += ["someone@{{cookiecutter.domain_name}}"]

DEFAULT_FROM_EMAIL = "Do Not Reply <do_not_reply@{{cookiecutter.domain_name}}>"

WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.elasticsearch7",
        "URLS": [env("ELASTICSEARCH_URL")],
        "INDEX": "wagtail",
        "TIMEOUT": 5,
        "OPTIONS": {},
        "INDEX_SETTINGS": {},
        "AUTO_UPDATE": False,
    }
}
