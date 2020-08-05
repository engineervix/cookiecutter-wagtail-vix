from django.db import models
from model_utils import Choices, FieldTracker
from model_utils.models import StatusModel, TimeStampedModel
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from phonenumber_field.modelfields import PhoneNumberField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet


@register_snippet
class People(index.Indexed, ClusterableModel, StatusModel, TimeStampedModel):
    """
    A Django model to store People objects.
    It uses the `@register_snippet` decorator to allow it to be accessible
    via the Snippets UI (e.g. /admin/snippets/base/people/)

    `People` uses the `ClusterableModel`, which allows the relationship with
    another model to be stored locally to the 'parent' model (e.g. a PageModel)
    until the parent is explicitly saved. This allows the editor to use the
    'Preview' button, to preview the content, without saving the relationships
    to the database.
    https://github.com/wagtail/django-modelcluster
    """

    first_name = models.CharField("First Name", max_length=254)
    last_name = models.CharField("Last Name", max_length=254)
    phone_number = PhoneNumberField("Phone Number")
    email_address = models.EmailField("Email Address")
    position = models.CharField("Position", max_length=254)
    bio = RichTextField(blank=True)
    facebook = models.URLField(
        "Facebook Link",
        max_length=254,
        blank=True,
        help_text="(Optional) Enter Facebook Profile Link, for example: https://www.facebook.com/conrad.mbewe.1",
    )
    twitter = models.URLField(
        "Twitter Link",
        max_length=254,
        blank=True,
        help_text="(Optional) Enter Twitter Profile Link, for example: https://twitter.com/voddiebaucham",
    )
    linked_in = models.URLField(
        "LinkedIn Link",
        max_length=254,
        blank=True,
        help_text="(Optional) Enter LinkedIn Profile Link, for example: https://www.linkedin.com/in/justin-lupele-phd-31a35092",
    )

    STATUS = Choices("draft", "published")

    # https://django-model-utils.readthedocs.io/en/latest/utilities.html#field-tracker
    tracker = FieldTracker()

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        # blank=True, # required
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        FieldPanel("status"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("first_name", classname="col6"),
                        FieldPanel("last_name", classname="col6"),
                    ]
                )
            ],
            "Name",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("phone_number", classname="col6"),
                        FieldPanel("email_address", classname="col6"),
                    ]
                )
            ],
            "Contact Details",
        ),
        FieldPanel("position"),
        FieldPanel("bio", classname="full"),
        ImageChooserPanel("image"),
        MultiFieldPanel(
            [
                FieldPanel("facebook", classname="full"),
                FieldPanel("twitter", classname="full"),
                FieldPanel("linked_in", classname="full"),
            ],
            "Social Media Links",
        ),
    ]

    search_fields = [
        index.SearchField("first_name", partial_match=True),
        index.SearchField("last_name", partial_match=True),
    ]

    @property
    def thumb_image(self):
        # Returns an empty string if there is no profile pic or the rendition
        # file can't be found.
        try:
            return self.image.get_rendition("fill-50x50").img_tag()
        except:  # noqa: E:722
            return ""

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
