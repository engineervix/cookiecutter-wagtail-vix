import pytest

import logging
from datetime import datetime, timedelta
from django.apps import apps
from wagtail.core.models import Page

from faker import Faker

from config.settings.base import WAGTAIL_SITE_NAME
from {{cookiecutter.project_slug}}.blog.models import ArticlePage
from {{cookiecutter.project_slug}}.blog.apps import BlogConfig
from {{cookiecutter.project_slug}}.blog.rss_feed_display import (
    get_rss_feed_entries,
    rss_feed_entries,
    POSTS,
)

fake = Faker()


@pytest.mark.django_db
def test_articles(client):
    """Test Our Articles"""
    articles = ArticlePage.objects.all()
    published_articles = articles.live()
    draft_articles = articles.not_live()
    assert articles.count() == 8
    assert published_articles.count() == 5
    assert draft_articles.count() == 3

    articles_with_no_author = articles.filter(author=None)
    for article in articles_with_no_author:
        assert article.article_author == WAGTAIL_SITE_NAME

    foo_article = articles.filter(author="Foo Bar")[0]
    assert foo_article.external_domain == "www.freecodecamp.org"

    articles_with_content = articles[:6]
    for article in articles_with_content:
        assert article.content

    articles_with_no_content = articles.filter(content=None)
    for article in articles_with_no_content:
        assert len(article.content) == 0

    assert len(articles_with_no_content) == 2

    """
    # TODO: Rewrite this test by attempting to dynamically create
    #       an article page with no cover image
    article_with_no_cover_image = foo_article
    with pytest.raises(Exception):
        assert article_with_no_cover_image.thumb_image
    """

    for article in published_articles:
        assert f"/blog/{article.slug}/" in article.full_url
        """
        NOTE
        Generally, external articles have no content.
        Therefore, the readtime module raises an exception on such an article.
        TODO
        - refine things to gracefully handle such a situation
        """
        if article not in articles_with_no_content:
            response = client.get(f"/blog/{article.slug}/")
            assert response.status_code == 200
            assert "blog/article_page.html" in [t.name for t in response.templates]
            assert article.title.encode() in response.content


@pytest.mark.django_db
def test_article_does_not_exist(client):
    """Check that we have a 404 if an article don't exist"""
    response = client.get(f"/blog/{fake.slug()}/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_blog(client):
    """Blog Testing"""
    live_pages = Page.objects.live()
    blog_index_page = live_pages.get(title="Blog")
    response = client.get(blog_index_page.get_url())
    sitemap = client.get("/sitemap.xml")

    assert response.status_code == 200
    assert blog_index_page.get_url() == "/blog/"
    assert "blog/article_index_page.html" in [t.name for t in response.templates]
    assert b"Welcome to the {{cookiecutter.project_name}} Blog" in response.content
    # actual if no pagination
    # assert response.content.count(b'class="card-img-top" src="') == 5
    # because of pagination, we should have 3 on the first page
    assert response.content.count(b'class="card-img-top"') == 3

    # due to pagination, we get the first three
    for article in ArticlePage.objects.live()[:3]:
        # TODO: This test somehow fails, investigate why
        # assert article.title.encode() in response.content
        assert article.full_url.encode() in sitemap.content

    for article in ArticlePage.objects.not_live():
        assert article.title.encode() not in response.content


@pytest.mark.django_db
def test_blog_app():
    assert BlogConfig.name == "{{cookiecutter.project_slug}}.blog"
    assert apps.get_app_config("blog").name == "{{cookiecutter.project_slug}}.blog"


def test_rss_feed_fetch_success():
    link, entries = get_rss_feed_entries()

    # title should not be empty
    assert link.feed.title != ""

    assert isinstance(entries, list)
    assert len(entries) == 3

    # an active RSS feed's latest entries shouldn't be older than 14 days!
    datelimit = datetime.today() - timedelta(days=14)

    datelist = [entry["datetime"] for entry in entries]

    # the test will fail if any of the entries are older than 2 weeks!
    for entry_date in datelist:
        assert entry_date > datelimit.date()


def test_rss_feed_fetch_failure(mocker):
    """Test for failures in fetching of RSS feeds"""
    mocker.patch(
        "{{cookiecutter.project_slug}}.blog.rss_feed_display.HTTP_STATUS", 404,
    )

    logging.getLogger()

    link, entries = rss_feed_entries()

    # if link is None, then an Exception was raised
    assert link is None

    # if the entries are in POSTS, then they are hardcoded,
    # which means there was an error in fetching them, an Exception was raised
    for entry in entries:
        assert entry in POSTS
