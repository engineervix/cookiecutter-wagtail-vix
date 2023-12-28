"""
Test settings

- Used to run tests fast on the continuous integration server and locally
"""

from email.utils import formataddr

from .base import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
# Turn debug off so tests run faster
DEBUG = False

TEMPLATES[0]["OPTIONS"]["debug"] = False  # noqa: F405

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/5.0/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY")  # noqa: F405

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

# In-memory email backend stores messages in django.core.mail.outbox
# for unit testing purposes
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

ADMINS.append(("Admin", "admin@example.com"))  # noqa: F405
LIST_OF_EMAIL_RECIPIENTS += list(map(lambda recipient: formataddr(recipient), ADMINS))  # noqa F405

# CACHING
# ------------------------------------------------------------------------------
# Speed advantages of in-memory caching without having to run Memcached
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# PASSWORD HASHING
# ------------------------------------------------------------------------------
# Use fast password hasher so tests run faster
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# See https://stackoverflow.com/questions/44160666/
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# OTHER
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = ["example.com"]
