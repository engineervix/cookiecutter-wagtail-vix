from typing import List

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    """Default user for {{ cookiecutter.project_name }}"""

    username = None
    email = models.EmailField(_("email address"), unique=True)

    name = models.CharField(blank=True, max_length=255)

    # TODO: check https://github.com/typeddjango/django-stubs/issues/174
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    # the email field and password will be required,
    # so they don’t need to go into the REQUIRED FIELDS list
    REQUIRED_FIELDS: List[str] = []

    def __str__(self):
        return self.email
