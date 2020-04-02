from django.db import models
from wagtail.core.models import Page


class HomePage(Page):
    search_fields = Page.search_fields


class AboutPage(Page):
    search_fields = Page.search_fields
    # Specifies parent to ArticlePage as being HomeeIndexPage
    parent_page_types = ["HomePage"]

    # Specifies what content types can exist as children of ArticlePage.
    # Empty list means that no child content types are allowed.
    subpage_types = []
