from django.test import TestCase

from {{cookiecutter.project_slug}}.users.factories import UserFactory
from {{cookiecutter.project_slug}}.users.models import User


class UserFactoryTestCase(TestCase):
    def test_create(self):
        assert User.objects.count() == 0

        user = UserFactory()

        assert isinstance(user, User)
        assert User.objects.count() == 1

        self.assertTrue(user.username)
        self.assertTrue(user.email)
        self.assertTrue(user.password)
        self.assertTrue(user.first_name)
        self.assertTrue(user.last_name)
