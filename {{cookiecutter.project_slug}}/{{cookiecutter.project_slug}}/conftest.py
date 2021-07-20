import random
import pytest
import wagtail_factories
import factory
from django.conf import settings
from faker import Faker
from faker_e164.providers import E164Provider  # E164 Phone Numbers
from yattag import Doc
from titlecase import titlecase
from wagtail.core.models import Site

from {{cookiecutter.project_slug}}.contact.models import (
    # ContactPage,
    ContactPagePhoneNumber,
    ContactPageEmailAddress,
)
from {{cookiecutter.project_slug}}.base.blocks import BaseStreamBlock
from {{cookiecutter.project_slug}}.tests.factories import (
    ArticleFactory,
    AboutPageFactory,
    ArticleIndexPageFactory,
    HomePageFactory,
    ContactPageFactory,
    PeopleFactory,
    UserFactory,
    SimpleDocFactory,
)

fake = Faker()
fake.add_provider(E164Provider)

doc, tag, text, line = Doc().ttl()


def fake_rich_text():
    """Uses yattag & Faker to Generate HTML text for testing Purposes"""
    # with tag("div", klass="rich-text"):
    for x in list(range(random.randint(2, 8))):
        with tag("p"):
            text(f"{str(x)} " + fake.paragraph())
    with tag("a", href=fake.uri()):
        text(fake.sentence())
    with tag("div", klass="photo-container"):
        doc.stag("img", src=fake.image_url(), klass="photo")
    with tag("p"):
        text(fake.paragraph())
    with tag("ul", id=f"{fake.word()}"):
        line("li", fake.sentence(), klass="priority")
        line("li", fake.word())
        line("li", fake.word())
        line("li", fake.word())
    with tag("p"):
        text(fake.paragraph())
    # doc.asis(
    #     f"""
    #         <table>
    #         <tr>
    #             <th>ID</th>
    #             <th>Item</th>
    #             <th>Description</th>
    #             <th>Comment</th>
    #         </tr>
    #         <tr>
    #             <td>0</td>
    #             <td>{fake.word()}</td>
    #             <td>{fake.word()}</td>
    #             <td>{fake.word()}</td>
    #         </tr>
    #         <tr>
    #             <td>1</td>
    #             <td>{fake.word()}</td>
    #             <td>{fake.word()}</td>
    #             <td>{fake.word()}</td>
    #         </tr>
    #         <tr>
    #             <td>2</td>
    #             <td>{fake.word()}</td>
    #             <td>{fake.word()}</td>
    #             <td>{fake.word()}</td>
    #         </tr>
    #         <tr>
    #             <td>3</td>
    #             <td>{fake.word()}</td>
    #             <td>{fake.word()}</td>
    #             <td>{fake.word()}</td>
    #         </tr>
    #         </table>
    #     """
    # )

    # print(indent(doc.getvalue()))
    return doc.getvalue()


def fake_embed_url():
    """
    Returns a random embed URL for testing Purposes.
    This is not an exhaustive oEmbed list. I just picked common providers. See
    https://github.com/wagtail/wagtail/blob/master/wagtail/embeds/oembed_providers.py
    for an exhaustive list
    """
    fake_dailymotion = "https://www.dailymotion.com/video/x55zbfz"
    fake_deviantart = (
        "https://www.deviantart.com/pixelstains/art/3-Foliage-Brushes-511087442"
    )
    fake_etsy = (
        "https://www.etsy.com/listing/157263100/travel-mugs-personalized-contigo-14-oz"
    )
    fake_facebook_post = "https://web.facebook.com/natgeo/posts/10157141227438951"
    fake_facebook_video = (
        "https://www.facebook.com/vietfunnyvideo/videos/a87e1b81/1395374707273324/"
    )
    fake_five_hundred_px = (
        "https://500px.com/photo/1010158024/The-End--by-Bruno-Desbois"
    )
    fake_flickr = "https://www.flickr.com/photos/phils-pixels/23032529294/"
    fake_github_gist = "https://gist.github.com/denji/8359866"
    # TODO: Instagram has issues. See https://github.com/wagtail/wagtail/issues/1985
    # fake_instagram = "https://www.instagram.com/p/CGU7hyJHf5B/"
    fake_issuu = "https://issuu.com/hellocapetown/docs/hct_jan_2020_issuu"
    fake_meetup = "https://www.meetup.com/RVALUG/events/hhgrkpybcdbtb/"
    fake_photobucket = "https://media.photobucket.com/user/MitziJ_photos/media/Snow2008026.jpg.html?filters[term]=snow&filters[primary]=images"
    fake_scribd = "https://www.scribd.com/book/257046945/Rust-The-Longest-War"
    fake_slideshare = (
        "https://www.slideshare.net/AlexanderLoechel/modern-python-testing"
    )
    fake_soundcloud = "https://soundcloud.com/ligonier/variant-on-benedictus"
    fake_speakerdeck = "https://speakerdeck.com/eitanlees/visualization"
    fake_ted = "https://www.ted.com/talks/michael_r_stiff_why_is_cotton_in_everything"
    fake_tumblr = "https://nom-food.tumblr.com/post/142794068868/mozzarella-chicken-in-tomato-sauce"
    fake_twitter = "https://twitter.com/jmwatt3/status/1223968429964701696"
    fake_vimeo = "https://vimeo.com/333599381"
    fake_youtube = "https://www.youtube.com/watch?v=oS-m5-XikwA"

    oembed_providers = [
        fake_dailymotion,
        fake_deviantart,
        fake_etsy,
        fake_facebook_post,
        fake_facebook_video,
        fake_five_hundred_px,
        fake_flickr,
        fake_github_gist,
        # fake_instagram,
        fake_issuu,
        fake_meetup,
        fake_photobucket,
        fake_scribd,
        fake_slideshare,
        fake_soundcloud,
        fake_speakerdeck,
        fake_ted,
        fake_tumblr,
        fake_twitter,
        fake_vimeo,
        fake_youtube,
    ]

    return random.choice(oembed_providers)


def fake_content():
    """
    Fake Article Content for testing Purposes
    The Article content is a StreamField, therefore it can consist
    of any combinations of individual StreamBlocks
    TODO:
        - [ ] Devise a test which uses parametrized data to test different
        combinations of the Streamblocks, including repeating of some blocks
    """
    fake_paragraph = fake_rich_text()
    fake_quote = {
        "text": fake.sentence(),
        "attribute_name": fake.name(),
    }
    fake_img = wagtail_factories.ImageFactory()
    three_random_words = fake.words(nb=3)
    fake_attribution = " ".join(three_random_words)

    data = [
        {"type": "paragraph_block", "value": fake_paragraph},
        {"type": "block_quote", "value": fake_quote},
        {"type": "embed_block", "value": fake_embed_url()},
        {
            "type": "heading_block",
            "value": {
                "heading_text": fake.sentence(),
                "size": random.choice(["h4", "h3", "h2"]),
            },
        },
        {
            "type": "table",
            "value": {
                "data": [
                    [fake.word(), fake.word(), fake.word()],
                    ["1", " ".join(fake.words(nb=3)), fake.word()],
                    ["2", " ".join(fake.words(nb=4)), fake.word()],
                    ["3", " ".join(fake.words(nb=3)), fake.word()],
                ],
                "cell": [],
                "first_row_is_table_header": True,
                "first_col_is_header": False,
                "table_caption": fake.sentence(),
            },
        },
        {
            "type": "image_block",
            "value": {
                "image": fake_img.id,
                "caption": random.choice(["", fake.sentence()]),
                "attribution": random.choice(["", titlecase(fake_attribution)]),
            },
        },
    ]

    content_block = BaseStreamBlock()
    content_block_value = content_block.to_python(data)
    return content_block_value


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker, tmpdir_factory):
    """
    Configure the DB for Testing.
    We also configure a MEDIA_ROOT temporary directory
    """
    media_dir = "_media_store"
    media_storage = tmpdir_factory.mktemp(media_dir)
    tmpdir_factory.mktemp(media_dir).join("images")
    tmpdir_factory.mktemp(media_dir).join("original_images")
    settings.MEDIA_ROOT = str(media_storage)
    with django_db_blocker.unblock():
        # create superuser
        UserFactory(
            is_staff=True, is_superuser=True,
        )
        root_page = wagtail_factories.PageFactory(parent=None)
        home_page = HomePageFactory(parent=root_page, title="Home", slug="home")
        # Create a Site with the new homepage set as the root
        Site.objects.all().delete()
        Site.objects.create(
            hostname="www.example.com",
            root_page=home_page,
            site_name="Test Site",
            is_default_site=True,
        )
        # create AboutPage
        # AboutPageFactory(parent=home_page, title="About", url_path="/about", slug="about")
        AboutPageFactory(parent=home_page, title="About", slug="about")
        # create BlogPage
        article_index_page = ArticleIndexPageFactory(
            parent=home_page,
            title="Blog",
            slug="blog",
            introduction=fake.text(max_nb_chars=254),
        )
        # create some Articles
        ArticleFactory(
            parent=article_index_page,
            live=True,
            article_type="Post",
            cover_picture=wagtail_factories.ImageFactory(),
            summary=fake.text(max_nb_chars=254),
            author=fake.name(),
            content=fake_content(),
        )
        ArticleFactory(
            parent=article_index_page,
            live=False,
            article_type="Post",
            cover_picture=wagtail_factories.ImageFactory(),
            summary=fake.text(max_nb_chars=254),
            author=fake.name(),
            content=fake_content(),
        )
        ArticleFactory(
            parent=article_index_page,
            live=True,
            article_type="Shout",
            cover_picture=wagtail_factories.ImageFactory(),
            summary=fake.text(max_nb_chars=254),
            content=fake_content(),
        )
        ArticleFactory(
            parent=article_index_page,
            live=True,
            article_type="Info",
            cover_picture=wagtail_factories.ImageFactory(),
            summary=fake.text(max_nb_chars=254),
            author=fake.name(),
            content=fake_content(),
        )
        ArticleFactory(
            parent=article_index_page,
            live=False,
            article_type="Info",
            cover_picture=wagtail_factories.ImageFactory(),
            summary=fake.text(max_nb_chars=254),
            content=fake_content(),
        )
        ArticleFactory(
            parent=article_index_page,
            live=True,
            article_type="Misc",
            cover_picture=wagtail_factories.ImageFactory(),
            summary=fake.text(max_nb_chars=254),
            content=fake_content(),
        )
        ArticleFactory(
            parent=article_index_page,
            live=True,
            article_type="URL",
            cover_picture=wagtail_factories.ImageFactory(),
            summary=fake.text(max_nb_chars=254),
            author=fake.name(),
            external_url=fake.uri(),
        )
        ArticleFactory(
            parent=article_index_page,
            live=False,
            article_type="URL",
            cover_picture=wagtail_factories.ImageFactory(),
            author="Foo Bar",
            summary=fake.text(max_nb_chars=254),
            external_url="https://www.freecodecamp.org/news/mechanical-engineering-to-software-developer/",
        )
        # Create People
        fake_phone_num = fake.e164(region_code="US", valid=True, possible=True)
        PeopleFactory.create_batch(
            size=4,
            image=wagtail_factories.ImageFactory(),
            phone_number=fake_phone_num,
            status="published",
        )
        PeopleFactory.create_batch(
            size=3,
            image=wagtail_factories.ImageFactory(),
            phone_number=fake_phone_num,
            status="draft",
        )
        PeopleFactory(
            # no image for this one
            phone_number=fake_phone_num,
            first_name="Jane",
            last_name="Doe",
            status="draft",
        )
        # create ContactPage
        contact_page = ContactPageFactory(
            parent=home_page,
            title="Contact",
            slug="contact",
            # address=fake.address()
        )
        # create contact details for ContactPage
        phone_01 = ContactPagePhoneNumber(
            phone_number=fake.e164(region_code="CA", valid=True, possible=True),
        )
        phone_02 = ContactPagePhoneNumber(
            phone_number=fake.e164(region_code="CA", valid=True, possible=True),
        )
        email_01 = ContactPageEmailAddress(email_address=fake.company_email,)
        email_02 = ContactPageEmailAddress(email_address=fake.company_email,)
        contact_page.phone_numbers = [phone_01, phone_02]
        contact_page.email_addresses = [email_01, email_02]
        contact_page.save()

        # add some documents
        doc1 = factory.django.FileField(filename="document_01.pdf")
        doc2 = factory.django.FileField(filename="document_02.pdf")
        SimpleDocFactory(title="Document 1", file=doc1)
        SimpleDocFactory(title="Document 2", file=doc2)
