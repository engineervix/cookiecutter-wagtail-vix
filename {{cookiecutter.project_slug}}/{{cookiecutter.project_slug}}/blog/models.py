import logging

# import traceback

from urllib.parse import urlparse

from django.contrib import messages
from django.db import models
from django.shortcuts import redirect, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# from model_utils import Choices, FieldTracker
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import Tag, TaggedItemBase
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

import readtime  # https://github.com/alanhamlett/readtime

# import bleach  # https://bleach.readthedocs.io

from config.settings.base import WAGTAIL_SITE_NAME

from {{cookiecutter.project_slug}}.base.blocks import BaseStreamBlock
from .rss_feed_display import get_rss_feed_entries as rss_feeds

logger = logging.getLogger(__name__)


class ArticleTag(TaggedItemBase):
    """
    This model allows us to create a many-to-many relationship between
    the ArticlePage object and tags. There's a longer guide on using it at
    http://docs.wagtail.io/en/latest/reference/pages/model_recipes.html#tagging
    """

    content_object = ParentalKey(
        "ArticlePage", related_name="tagged_items", on_delete=models.CASCADE
    )


class ArticlePage(Page):
    """
    TODO
        - [x] Add a Summary / Synopsis field to this Model
        - [ ] Rethink the distinction between external URL and internal articles
    """

    summary = models.TextField(
        "Summary", help_text="Text to summarise / describe the article"
    )
    cover_picture = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        # blank=True, # required
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
    )
    content = StreamField(
        BaseStreamBlock(),
        help_text='Leave this Blank if Article Type is "External Link"',
        verbose_name="Content",
        null=True,
        blank=True,
    )
    # subtitle = models.CharField(blank=True, max_length=255)
    tags = ClusterTaggableManager(through=ArticleTag, blank=True)
    date_published = models.DateField("Article Date", max_length=254)
    author = models.CharField("Author", max_length=254, null=True, blank=True)

    ARTICLE_TYPES = (
        ("Shout", "Announcement"),
        ("Post", "Article"),
        ("Info", "Notice"),
        ("URL", "External Link"),
        ("Misc", "Other"),
    )

    article_type = models.CharField(max_length=5, choices=ARTICLE_TYPES)
    external_url = models.URLField(
        "External Link",
        help_text="Only Add Link if Article is an External Link",
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("summary", classname="full"),
        MultiFieldPanel(
            [FieldPanel("date_published"), FieldPanel("tags")],
            heading="Article information",
        ),
        FieldPanel("author"),
        FieldPanel("article_type"),
        ImageChooserPanel("cover_picture"),
        StreamFieldPanel("content"),
        FieldPanel("external_url"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("author", partial_match=True),
        index.SearchField("content", partial_match=True),
    ]

    # https://stackoverflow.com/a/51936342 on using @property decorators

    @property
    def external_domain(self):
        # Returns a custom string if there's a problem in parsing external_url
        parsed_uri = urlparse(self.external_url)
        return parsed_uri.netloc if parsed_uri.netloc != "" else "another website"

    @property
    def article_author(self):
        # Returns a custom string if author field is blank
        if self.author is None:
            return WAGTAIL_SITE_NAME
        else:
            return self.author

    @property
    def thumb_image(self):
        # Returns an empty string if there is no profile pic or the rendition
        # file can't be found.
        try:
            return self.cover_picture.get_rendition("fill-50x50").img_tag()
        except:  # noqa: E:722
            # TODO: - Return a default image instead of empty string
            #       - refine the try...except: Avoid "wildcard" Exception handling
            return ""

    @property
    def get_tags(self):
        """
        We're returning all the tags that are related to the article into a
        list we can access on the template. We're additionally adding a URL to
        access ArticlePage objects with that tag
        """
        tags = self.tags.all()
        for tag in tags:
            tag.url = "/" + "/".join(
                s.strip("/") for s in [self.get_parent().url, "tags", tag.slug]
            )
        return tags

    # Specifies parent to ArticlePage as being ArticleIndexPages
    parent_page_types = ["ArticleIndexPage"]

    # Specifies what content types can exist as children of ArticlePage.
    # Empty list means that no child content types are allowed.
    subpage_types = []

    def get_context(self, request):
        # context = super().get_context(request)
        context = super(ArticlePage, self).get_context(request)
        context["time_to_read"] = readtime.of_html(self.content.__html__())
        return context
        # return render(request, 'blog/article_page.html', context)


class ArticleIndexPage(RoutablePageMixin, Page):
    """
    Index page for articles.
    We need to alter the page model's context to return the child page objects,
    the ArticlePage objects, so that it works as an index page

    RoutablePageMixin is used to allow for a custom sub-URL for the tag views
    defined above.
    """

    # Specifies parent to ArticlePage as being MediaPage
    # parent_page_types = ['MediaPage']

    # Specifies what content types can exist as children of ArticlePage.
    # Empty list means that no child content types are allowed.
    # subpage_types = []
    introduction = models.TextField(help_text="Text to describe the page")

    content_panels = Page.content_panels + [
        FieldPanel("introduction", classname="full"),
    ]

    # Specifies parent to ArticleIndexPages as being HomPage
    parent_page_types = ["home.HomePage"]

    # Speficies that only ArticlePage objects can live under this index page
    subpage_types = ["ArticlePage"]

    # Defines a method to access the children of the page (e.g. ArticlePage
    # objects).
    def children(self):
        return self.get_children().specific().live()

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    # http://docs.wagtail.io/en/latest/getting_started/tutorial.html#overriding-context
    def get_context(self, request):
        # context = super().get_context(request)
        context = super(ArticleIndexPage, self).get_context(request)
        # get all articles
        all_articles = (
            ArticlePage.objects.descendant_of(self).live().order_by("-date_published")
        )
        # Paginate all posts by 3 per page
        paginator = Paginator(all_articles, 3)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            articles = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            articles = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            articles = paginator.page(paginator.num_pages)

        # "articles" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["articles"] = articles
        # context["articles"] = (
        #     ArticlePage.objects.descendant_of(self).live().order_by("-date_published")
        # )
        context["rss_feeds"] = rss_feeds
        return context

    # This defines a Custom view that utilizes Tags. This view will return all
    # related ArticlePages for a given Tag or redirect back to the
    # ArticleIndexPage. More information on RoutablePages is at
    # http://docs.wagtail.io/en/latest/reference/contrib/routablepage.html
    @route(r"^tags/$", name="tag_archive")
    @route(r"^tags/([\w-]+)/$", name="tag_archive")
    def tag_archive(self, request, tag=None):

        try:
            tag = Tag.objects.get(slug=tag)
        except Tag.DoesNotExist:
            if tag:
                msg = 'There are no articles tagged with "{}"'.format(tag)
                messages.add_message(request, messages.INFO, msg)
            return redirect(self.url)

        articles = self.get_articles(tag=tag)
        context = {"tag": tag, "articles": articles}
        return render(request, "blog/article_index_page.html", context)

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    # Returns the child ArticlePage objects for this ArticlePageIndex.
    # If a tag is used then it will filter the articles by tag.
    def get_articles(self, tag=None):
        articles = ArticlePage.objects.live().descendant_of(self)
        if tag:
            articles = articles.filter(tags=tag)
        return articles

    # Returns the list of Tags for all child articles of this ArticlePage.
    def get_child_tags(self):
        tags = []
        for article in self.get_articles():
            # Not tags.append() because we don't want a list of lists
            tags += article.get_tags
        tags = sorted(set(tags))
        return tags
