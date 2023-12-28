"""See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/"""

import logging
from email.utils import formataddr, getaddresses

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.redis import RedisIntegration

from .base import *  # noqa

DEBUG = False  # just to make sure!

DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)  # noqa F405

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env("REDIS_URL"),  # noqa F405
        "KEY_PREFIX": env("REDIS_KEY_PREFIX"),  # noqa F405
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # Mimicing memcache behavior.
            # https://github.com/jazzband/django-redis#memcached-exceptions-behavior
            "IGNORE_EXCEPTIONS": True,
        },
    },
    "renditions": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": env("MEMCACHED_URL"),  # noqa F405
        "TIMEOUT": 600,
    },
}

# RQ_QUEUES = {
#     "default": {
#         "USE_REDIS_CACHE": "default",
#     },
# }

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# https://docs.wagtail.org/en/latest/reference/settings.html#wagtail-redirects-file-storage
# By default the redirect importer keeps track of the uploaded file as a temp file,
# but on certain environments (load balanced/cloud environments), you cannot
# keep a shared file between environments.
# For those cases you can use the built-in cache to store the file instead.
WAGTAIL_REDIRECTS_FILE_STORAGE = "cache"

# https://docs.wagtail.org/en/stable/reference/contrib/frontendcache.html#cloudflare
INSTALLED_APPS += ["wagtail.contrib.frontend_cache"]  # noqa: F405
WAGTAILFRONTENDCACHE = {
    "cloudflare": {
        "BACKEND": "wagtail.contrib.frontend_cache.backends.CloudflareBackend",
        "BEARER_TOKEN": env("CLOUDFLARE_BEARER_TOKEN"),  # noqa F405
        "ZONEID": env("CLOUDFLARE_DOMAIN_ZONE_ID"),  # noqa F405
    },
}

# SECURITY
# ------------------------------------------------------------------------------

# if the next two settings are controlled by nginx, comment them out
# https://docs.djangoproject.com/en/5.0/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# https://docs.djangoproject.com/en/5.0/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)  # noqa F405
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SAMESITE = "None"
# if the next set of settings are controlled by nginx, comment them out
# https://docs.djangoproject.com/en/5.0/topics/security/#ssl-https
# https://docs.djangoproject.com/en/5.0/ref/settings/#secure-hsts-seconds
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
# SECURE_HSTS_SECONDS = 518400
# https://docs.djangoproject.com/en/5.0/ref/settings/#secure-hsts-include-subdomains
# SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)  # noqa F405
# https://docs.djangoproject.com/en/5.0/ref/settings/#secure-hsts-preload
# SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)  # noqa F405
# https://docs.djangoproject.com/en/5.0/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = env.bool("DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True)  # noqa F405

# ==============================================================================
# incorporationg Backblaze B2 Cloud Storage
# ref: https://github.com/jschneier/django-storages/issues/765#issuecomment-699487715
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_ACCESS_KEY_ID = os.getenv('B2_USER')
# AWS_SECRET_ACCESS_KEY = os.getenv('B2_KEY')
# AWS_STORAGE_BUCKET_NAME = os.getenv('B2_BUCKET')
# AWS_S3_CUSTOM_DOMAIN = 'f002.backblazeb2.com/file/B2_BUCKET'
# AWS_S3_ENDPOINT_URL = 'https://B2_BUCKET.s3.us-west-002.backblazeb2.com' # exact url stated in b2 bucket overview page
# ==============================================================================

# STORAGES
# ------------------------------------------------------------------------------
# https://django-storages.readthedocs.io/en/latest/#installation
INSTALLED_APPS += ["storages"]  # noqa: F405
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")  # noqa: F405
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")  # noqa: F405
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")  # noqa: F405
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = env("AWS_S3_FILE_OVERWRITE", default=False)  # noqa: F405
# DO NOT change these unless you know what you're doing.
_AWS_EXPIRY = 60 * 60 * 24 * 7
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": f"max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate"}
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME", default=None)  # noqa: F405
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#cloudfront
AWS_S3_CUSTOM_DOMAIN = env("AWS_S3_CUSTOM_DOMAIN", default=None)  # noqa: F405
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_S3_ENDPOINT_URL = env("AWS_S3_ENDPOINT_URL")  # noqa: F405
aws_s3_domain = AWS_S3_CUSTOM_DOMAIN or f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.backblaze.com"

# STATIC
# ------------------------
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
# Temporary hack if you experience problems: https://stackoverflow.com/a/69123932
# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
#     },
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedStaticFilesStoragee",
#     },
# }

# MEDIA
# ------------------------------------------------------------------------------
MEDIA_URL = f"https://{aws_s3_domain}/files/"

# setup email backend via Anymail
# ------------------------------------------------------------------------------
# https://anymail.readthedocs.io/en/stable/installation/#installing-anymail
INSTALLED_APPS += ["anymail"]  # noqa F405
# https://docs.djangoproject.com/en/5.0/ref/settings/#email-backend
# https://anymail.readthedocs.io/en/stable/installation/#anymail-settings-reference
# https://anymail.readthedocs.io/en/stable/esps/sendgrid/
EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
ANYMAIL = {
    "SENDGRID_API_KEY": env("SENDGRID_API_KEY"),  # noqa F405
    "SENDGRID_GENERATE_MESSAGE_ID": env("SENDGRID_GENERATE_MESSAGE_ID"),  # noqa F405
    "SENDGRID_MERGE_FIELD_FORMAT": env("SENDGRID_MERGE_FIELD_FORMAT"),  # noqa F405
    "SENDGRID_API_URL": env("SENDGRID_API_URL", default="https://api.sendgrid.com/v3/"),  # noqa F405
}

if len(getaddresses([env("EMAIL_RECIPIENTS")])) == 1:  # noqa F405
    ADMINS.append(getaddresses([env("EMAIL_RECIPIENTS")])[0])  # noqa F405  # noqa F405
else:
    recipients = getaddresses([env("EMAIL_RECIPIENTS")])  # noqa F405
    ADMINS += recipients  # noqa F405

LIST_OF_EMAIL_RECIPIENTS += list(map(lambda recipient: formataddr(recipient), ADMINS))  # noqa F405
email_address = getaddresses([env("DEFAULT_FROM_EMAIL")])[0]  # noqa F405
DEFAULT_FROM_EMAIL = formataddr(email_address)

# https://docs.djangoproject.com/en/5.0/ref/settings/#server-email
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)  # noqa F405

# https://docs.djangoproject.com/en/5.0/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = env(  # noqa F405
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="[{{ cookiecutter.project_name }}]",
)

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.0/ref/settings/#logging
# See https://docs.djangoproject.com/en/5.0/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {"format": "%(levelname)s %(asctime)s %(module)s " "%(process)d %(thread)d %(message)s"},
        # "rq_console": {
        #     "format": "%(asctime)s %(message)s",
        #     "datefmt": "%H:%M:%S",
        # },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        # "rq_console": {
        #     "level": "DEBUG",
        #     "class": "rq.logutils.ColorizingStreamHandler",
        #     "formatter": "rq_console",
        #     "exclude": ["%(asctime)s"],
        # },
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
        # "rq.worker": {"handlers": ["rq_console"], "level": "DEBUG"},
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
