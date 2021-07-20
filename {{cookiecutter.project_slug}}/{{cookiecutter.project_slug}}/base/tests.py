import pytest

from django.apps import apps

# from django import urls
from wagtail.core.models import Site

from {{cookiecutter.project_slug}}.base.models import People
from {{cookiecutter.project_slug}}.base.apps import BaseConfig


@pytest.mark.django_db
def test_site():
    """There should only be 1 instance of a Wagtail Site."""
    assert Site.objects.count() == 1


@pytest.mark.django_db
def test_people():
    """Tests the People Snippet"""
    people = People.objects.all()
    assert people.count() == 8
    assert people.filter(status="published").count() == 4
    assert people.filter(status="draft").count() == 4
    for person in people[:7]:
        assert person.thumb_image != ""
    jane_doe = people.last()  # the last person (Jane Doe) has no image
    with pytest.raises(Exception):
        assert jane_doe.thumb_image


@pytest.mark.django_db
def test_base_app():
    assert BaseConfig.name == "{{cookiecutter.project_slug}}.base"
    assert apps.get_app_config("base").name == "{{cookiecutter.project_slug}}.base"


def test_with_logged_in_admin(admin_client):
    # client.login(username=admin_user.username, password=admin_user.password)
    response = admin_client.get("/admin/blog/articlepage/")
    assert (
        b'<a href="/admin/blog/articlepage/create/" class="button bicolor icon icon-plus" title="Add a new article page">Add article page</a>'
        in response.content
    )


@pytest.mark.django_db
def test_redirect_to_login_when_logged_out(client):
    """Verify we redirect to the login page when a user is not logged in"""
    url = "/admin/blog/articlepage/"
    resp = client.get(url)
    assert resp.status_code == 302
    assert resp.url == "/admin/login/?next=/admin/blog/articlepage/"


@pytest.mark.django_db
def test_document_serve(client):
    """Test Serving of PDF Documents"""
    # TODO: Parametrize this
    url1 = "/document/view/1/document_01.pdf"
    url2 = "/document/view/2/document_02.pdf"
    response1 = client.get(url1)
    response2 = client.get(url2)
    assert response1.status_code == 200
    assert response2.status_code == 200
    assert "attachment" not in response1.get("Content-Disposition")
    assert "attachment" not in response2.get("Content-Disposition")
    assert response1.get("Content-Type") == "application/pdf"
    assert response2.get("Content-Type") == "application/pdf"
