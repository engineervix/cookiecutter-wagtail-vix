from .base import *

# Django Debug Toolbar
INSTALLED_APPS.append(  # noqa: F405
    "debug_toolbar"
)  # https://github.com/jazzband/django-debug-toolbar

# Additional middleware introduced by debug toolbar
# insert after first element value.

# The order of MIDDLEWARE and MIDDLEWARE_CLASSES is important.
# You should include the Debug Toolbar middleware as early as possible in the list.
# However, it must come after any other middleware that encodes the response's content,
# such as GZipMiddleware.
MIDDLEWARE.insert(1, "debug_toolbar.middleware.DebugToolbarMiddleware")  # noqa: F405

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ["127.0.0.1", "::1"]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR.path("templates"))],  # noqa: F405
        # 'APP_DIRS': True,  # default setting
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",  # non-default
                "django.template.context_processors.media",  # non-default
                "django.template.context_processors.static",  # non-default
                "django.template.context_processors.tz",  # non-default
                # "maintenance_mode.context_processors.maintenance_mode"
            ],
            "loaders": [  # <-- this wasn't there in default config
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    }
]

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

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = "localhost"
# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 1025

LIST_OF_EMAIL_RECIPIENTS += ["someone@{{cookiecutter.domain_name}}"]  # noqa: F405

DEFAULT_FROM_EMAIL = "Do Not Reply <do_not_reply@{{cookiecutter.domain_name}}>"

WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.contrib.postgres_search.backend",
        "SEARCH_CONFIG": "english",
        "ATOMIC_REBUILD": True,
    },
}

# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-eager-propagates
# CELERY_TASK_EAGER_PROPAGATES = True
