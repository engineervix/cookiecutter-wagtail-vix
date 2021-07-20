"""See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/"""

import logging
from email.utils import formataddr, getaddresses

import sentry_sdk
# from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.redis import RedisIntegration

from .base import *  # noqa

DEBUG = False  # just to make sure!

DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)  # noqa F405

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR.path("templates"))],  # noqa F405
        # 'APP_DIRS': True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
            ],
            "loaders": [  # <-- this wasn't there in default config
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                    ],
                ),
            ],
        },
    },
]

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env("REDIS_URL"),  # noqa F405
        "KEY_PREFIX": env("REDIS_KEY_PREFIX"),  # noqa F405
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SERIALIZER": "django_redis.serializers.msgpack.MSGPackSerializer",
            # "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            "COMPRESSOR": "django_redis.compressors.lz4.Lz4Compressor",
        },
    },
    "renditions": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": env("MEMCACHED_URL"),  # noqa F405
        "TIMEOUT": 600,
        "OPTIONS": {"MAX_ENTRIES": 1000},
    },
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

WAGTAILFRONTENDCACHE = {
    "cloudflare": {
        "BACKEND": "wagtail.contrib.frontend_cache.backends.CloudflareBackend",
        "BEARER_TOKEN": env("CLOUDFLARE_BEARER_TOKEN"),  # noqa F405
        "ZONEID": env("CLOUDFLARE_DOMAIN_ZONE_ID"),  # noqa F405
    },
}

USER_AGENTS_CACHE = "default"

# Obviously these three settings are needed when SSL is on
# SECURE_PROXY_SSL_HEADER is controlled by nginx so no need
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# setup email backend via Anymail
# ------------------------------------------------------------------------------
# https://anymail.readthedocs.io/en/stable/installation/#installing-anymail
INSTALLED_APPS += ["anymail"]  # noqa F405
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# https://anymail.readthedocs.io/en/stable/installation/#anymail-settings-reference
# https://anymail.readthedocs.io/en/stable/esps/sendgrid/
EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
ANYMAIL = {
    "SENDGRID_API_KEY": env("SENDGRID_API_KEY"),  # noqa F405
    "SENDGRID_GENERATE_MESSAGE_ID": env("SENDGRID_GENERATE_MESSAGE_ID"),  # noqa F405
    "SENDGRID_MERGE_FIELD_FORMAT": env("SENDGRID_MERGE_FIELD_FORMAT"),  # noqa F405
    "SENDGRID_API_URL": env(  # noqa F405
        "SENDGRID_API_URL", default="https://api.sendgrid.com/v3/"
    ),
}

if len(getaddresses([env("EMAIL_RECIPIENTS")])) == 1:  # noqa F405
    LIST_OF_EMAIL_RECIPIENTS.append(  # noqa F405
        formataddr(getaddresses([env("EMAIL_RECIPIENTS")])[0])  # noqa F405
    )
else:
    for email_address in getaddresses([env("EMAIL_RECIPIENTS")]):  # noqa F405
        LIST_OF_EMAIL_RECIPIENTS += formataddr(email_address)  # noqa F405

email_address = getaddresses([env("DEFAULT_FROM_EMAIL")])[0]  # noqa F405
DEFAULT_FROM_EMAIL = formataddr(email_address)

# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)  # noqa F405

# enable SSL flag, if the data exchange needs to be secure.
# Not needed for small apps
RECAPTCHA_USE_SSL = True

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
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
    "loggers": {
        "django.db.backends": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
        # Errors logged by the SDK itself
        "sentry_sdk": {"level": "ERROR", "handlers": ["console"], "propagate": False},
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}

# Sentry
# ------------------------------------------------------------------------------
SENTRY_DSN = env("SENTRY_DSN")  # noqa F405
SENTRY_LOG_LEVEL = env.int("DJANGO_SENTRY_LOG_LEVEL", logging.INFO)  # noqa F405

sentry_logging = LoggingIntegration(
    level=SENTRY_LOG_LEVEL,  # Capture info and above as breadcrumbs
    event_level=logging.ERROR,  # Send errors as events
)
integrations = [
    sentry_logging,
    DjangoIntegration(),
    # CeleryIntegration(),
    RedisIntegration(),
]
sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=integrations,
    environment=env("SENTRY_ENVIRONMENT", default="production"),  # noqa F405
    traces_sample_rate=env.float("SENTRY_TRACES_SAMPLE_RATE", default=0.0),  # noqa F405
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
