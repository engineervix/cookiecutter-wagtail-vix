import pytest

from django.apps import apps
from wagtail.core.models import Page

from {{cookiecutter.project_slug}}.base.models import People
from {{cookiecutter.project_slug}}.home.apps import HomeConfig


@pytest.mark.django_db
def test_homepage(client):
    """Tests the rendering of the custom homepage."""
    live_pages = Page.objects.live()
    home_page = live_pages.get(title="Home")
    response = client.get(home_page.get_url())
    assert response.status_code == 200
    assert home_page.get_url() == "/"
    assert "home/home_page.html" in [t.name for t in response.templates]
    assert b"Beverly Hills, CA 90210" in response.content


@pytest.mark.django_db
def test_aboutpage(client):
    """Tests the rendering of the about_page."""
    live_pages = Page.objects.live()
    about_page = live_pages.get(title="About")
    response = client.get(about_page.get_url())
    assert response.status_code == 200
    assert about_page.get_url() == "/about/"
    assert "home/about_page.html" in [t.name for t in response.templates]
    assert b"Meet the team working tirelessly" in response.content
    assert response.content.count(b'class="card-img-top"') == 4
    people = People.objects.all().filter(status="published")
    for person in people:
        assert person.first_name.encode() in response.content
    draft_people = People.objects.all().filter(status="draft")
    for person in draft_people:
        assert person.twitter.encode() not in response.content


@pytest.mark.django_db
def test_home_app():
    assert HomeConfig.name == "{{cookiecutter.project_slug}}.home"
    assert apps.get_app_config("home").name == "{{cookiecutter.project_slug}}.home"
