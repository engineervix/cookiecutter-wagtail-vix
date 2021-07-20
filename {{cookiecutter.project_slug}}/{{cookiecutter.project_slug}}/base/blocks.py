from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """

    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/image_block.html"


class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h4 sizes for headers
    """

    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Select a header size"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"


class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows the user to attribute a quote to an author
    """

    text = TextBlock()
    attribute_name = CharBlock(blank=True, required=False, label="e.g. Mary Berry")

    class Meta:
        icon = "fa-quote-left"
        template = "blocks/blockquote.html"


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """

    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        icon="fa-paragraph", template="blocks/paragraph_block.html"
    )
    image_block = ImageBlock()
    block_quote = BlockQuote()
    embed_block = EmbedBlock(
        help_text="Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks",
        icon="media",
        template="blocks/embed_block.html",
    )
    table = TableBlock(
        template="blocks/table_block.html",
    )

    class Meta:
        required = False


class CustomRichTextBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """

    paragraph_block = RichTextBlock(
        icon="fa-paragraph", template="blocks/paragraph_block.html", editor="simple"
    )

    def get_api_representation(self, value, context=None):
        # this hack based on https://github.com/wagtail/wagtail/issues/2695#issuecomment-457392434
        api_representation = super().get_api_representation(value, context)
        # we don't want the 'id
        key_to_be_deleted = "id"
        api_representation.pop(key_to_be_deleted, None)
        api_representation["paragraph_block"] = str(value["paragraph_block"])
        return api_representation
