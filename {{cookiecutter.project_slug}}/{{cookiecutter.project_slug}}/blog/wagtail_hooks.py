"""
N.B. To see what icons are available for use in Wagtail menus and StreamField
block types, enable the styleguide in settings:

INSTALLED_APPS = (
   ...
   'wagtail.contrib.styleguide',
   ...
)

or see http://kave.github.io/general/2015/12/06/wagtail-streamfield-icons.html

This project includes the full font-awesome set, so the entire
font-awesome icon set is available to you. Options are at http://fontawesome.io/icons/.
"""

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import ArticlePage


class ArticlesModelAdmin(ModelAdmin):
    model = ArticlePage
    menu_label = "Articles"  # ditch this to use verbose_name_plural from model
    menu_icon = "fa-newspaper-o"  # change as required
    add_to_settings_menu = False
    list_display = ("title", "article_type", "date_published", "live")
    list_filter = ("article_type", "live")
    ordering = ("-first_published_at",)
    list_per_page = 10
    search_fields = ("title", "content", "author")


# Now we just need to register our customised ModelAdmin class with Wagtail
modeladmin_register(ArticlesModelAdmin)
