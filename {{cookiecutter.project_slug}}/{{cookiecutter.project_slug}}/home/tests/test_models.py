import wagtail_factories
from wagtail.models import Site
from wagtail.test.utils import WagtailPageTestCase

from {{cookiecutter.project_slug}}.home.factories import HomePageFactory


class HomePageTestCase(WagtailPageTestCase):
    @classmethod
    def setUpTestData(cls):
        root = wagtail_factories.PageFactory(parent=None)
        cls.page = HomePageFactory(parent=root)

        hostname = "example.com"
        Site.objects.all().delete()
        Site.objects.create(
            hostname=hostname,
            root_page=cls.page,
            site_name="Test Site",
            is_default_site=True,
        )

    def test_route(self):
        self.assertPageIsRoutable(self.page)

    def test_rendering(self):
        self.assertPageIsRenderable(self.page)

    def test_editability(self):
        self.assertPageIsEditable(self.page)

    def test_general_previewability(self):
        self.assertPageIsPreviewable(self.page)
