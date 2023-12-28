import wagtail_factories

from {{cookiecutter.project_slug}}.home.models import HomePage


class HomePageFactory(wagtail_factories.PageFactory):
    title = "Home"

    class Meta:
        model = HomePage
