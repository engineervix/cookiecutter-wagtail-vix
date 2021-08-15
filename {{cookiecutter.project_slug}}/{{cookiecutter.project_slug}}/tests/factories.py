import random
import wagtail_factories
import factory
from wagtail.core import blocks
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.embeds.blocks import EmbedBlock

# from factory import fuzzy
from {{cookiecutter.project_slug}}.base.models import People
from {{cookiecutter.project_slug}}.base.blocks import HeadingBlock, ImageBlock, BlockQuote

from {{cookiecutter.project_slug}}.blog.models import ArticlePage, ArticleIndexPage

from {{cookiecutter.project_slug}}.users.models import User
from {{cookiecutter.project_slug}}.contact.models import ContactPage
from {{cookiecutter.project_slug}}.home.models import AboutPage, HomePage

# from django.utils.timezone import now


class HomePageFactory(wagtail_factories.PageFactory):
    """HomePage Factory"""

    class Meta:
        model = HomePage


class AboutPageFactory(wagtail_factories.PageFactory):
    """AboutPage Factory"""

    class Meta:
        model = AboutPage


class ArticleIndexPageFactory(wagtail_factories.PageFactory):
    """ArticleIndexPage Factory"""

    class Meta:
        model = ArticleIndexPage


class ContactPageFactory(wagtail_factories.PageFactory):
    """ContactPage Factory"""

    address = factory.Faker("address")

    class Meta:
        model = ContactPage


class UserFactory(factory.django.DjangoModelFactory):
    """Factory for creating Django User objects"""

    # username = factory.Faker("user_name")
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.Faker("password")
    # is_staff = True
    # is_superuser = True

    class Meta:
        model = User


class PeopleFactory(factory.django.DjangoModelFactory):
    """Factory for creating People objects"""

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email_address = factory.Faker("company_email")
    position = factory.Faker("job")
    bio = factory.Faker("text")
    facebook = factory.LazyAttribute(
        lambda o: f"https://www.facebook.com/{o.first_name.lower()}_{o.last_name.lower()}"
    )
    twitter = factory.LazyAttribute(
        lambda o: f"https://www.twitter.com/{o.first_name.lower()}_{o.last_name.lower()}"
    )
    linked_in = factory.LazyAttribute(
        lambda o: f"https://www.linkedin.com/in/{o.first_name.lower()}_{o.last_name.lower()}"
    )
    # status = fuzzy.FuzzyChoice(['draft', 'published'])

    class Meta:
        model = People


# class ArticleTagFactory(factory.django.DjangoModelFactory):
#     """Article Tags"""

#     class Meta:
#         model = ArticleTag


class ArticleFactory(wagtail_factories.PageFactory):
    """Factory for Making Article objects"""

    title = factory.Faker("paragraph")
    date_published = factory.Faker("date_between", start_date="-3y", end_date="today")
    # author = factory.Faker("name")
    # tags  # depends on ArticleTagFactory
    # article_type = fuzzy.FuzzyChoice(['Shout', 'Post', 'Info', 'URL', 'Misc'])
    # external_url = factory.Faker("uri")
    # cover_picture
    # content = factory.Faker("text")

    class Meta:
        model = ArticlePage


class SimpleDocFactory(wagtail_factories.DocumentFactory):
    """Factory for creating Wagtail Documents"""

    # file = factory.django.FileField(filename=f'{factory.Faker("slug")}.pdf')


# class HeadingBlockFactory(wagtail_factories.StructBlockFactory):
#     heading_text = factory.Faker(
#         "text", max_nb_chars=200
#     ).generate(extra_kwargs={})
#     size = random.choice(['h2', 'h3', 'h4'])

#     class Meta:
#         model = HeadingBlock


# class ImageBlockFactory(wagtail_factories.StructBlockFactory):
#     image = factory.SubFactory(wagtail_factories.ImageChooserBlockFactory)
#     caption = random.choice([factory.Faker("text"), ""])
#     attribution = random.choice([factory.Faker("text", max_nb_chars=200).generate(extra_kwargs={}), ""])

#     class Meta:
#         model = ImageBlock


# class BlockQuoteFactory(wagtail_factories.StructBlockFactory):
#     text = factory.Faker("text")
#     attribute_name = attribution = random.choice([factory.Faker("text", max_nb_chars=200).generate(extra_kwargs={}), ""])

#     class Meta:
#         model = BlockQuote


# class ChoiceBlockFactory(wagtail_factories.blocks.BlockFactory):

#     class Meta:
#         model = blocks.ChoiceBlock


# class TextBlockFactory(wagtail_factories.blocks.BlockFactory):

#     class Meta:
#         model = blocks.TextBlock


# class EmbedBlockFactory(wagtail_factories.blocks.BlockFactory):

#     class Meta:
#         model = EmbedBlock


# class RichTextBlockFactory(wagtail_factories.blocks.BlockFactory):

#     class Meta:
#         model = blocks.RichTextBlock


# class TableBlockFactory(wagtail_factories.blocks.BlockFactory):

#     class Meta:
#         model = TableBlock
