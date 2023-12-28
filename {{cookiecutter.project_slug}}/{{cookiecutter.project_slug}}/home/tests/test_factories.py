from django.test import TestCase

from {{cookiecutter.project_slug}}.home.factories import HomePageFactory
from {{cookiecutter.project_slug}}.home.models import HomePage


class HomePageFactoryTestCase(TestCase):
    def test_create(self):
        assert HomePage.objects.count() == 0

        home = HomePageFactory()

        assert isinstance(home, HomePage)
        assert HomePage.objects.count() == 1
        assert home.title == "Home"
        assert home.slug == "home"
