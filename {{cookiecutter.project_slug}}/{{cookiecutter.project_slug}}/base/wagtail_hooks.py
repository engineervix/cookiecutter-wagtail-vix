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

from {{cookiecutter.project_slug}}.base.models import People


class PeopleModelAdmin(ModelAdmin):
    model = People
    menu_label = "People"  # ditch this to use verbose_name_plural from model
    menu_icon = "fa-users"  # change as required
    list_display = ("first_name", "last_name", "position", "thumb_image", "status")
    list_filter = ("position", "status")
    search_fields = ("first_name", "last_name")


# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(PeopleModelAdmin)
