import wagtail_factories
from django.test import TestCase
from django.urls import reverse
from wagtail.models import Page, Site

from {{cookiecutter.project_slug}}.home.factories import HomePageFactory


class SiteSearchTestCase(TestCase):
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

    def test_site_search_with_results(self):
        # Create a search query
        search_query = "Home"

        # Simulate a GET request to the search view
        response = self.client.get(reverse("search"), {"query": search_query})

        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, 200)

        # Check that the search results are present in the response context
        self.assertIn("search_results", response.context)

        # Check that the search query is present in the response context
        self.assertEqual(response.context["search_query"], search_query)

    def test_site_search_without_results(self):
        # Create a search query that will not yield any results
        search_query = "Lorem Ipsum"

        # Simulate a GET request to the search view
        response = self.client.get(reverse("search"), {"query": search_query})

        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, 200)

        # Check that the search results are an empty queryset
        self.assertQuerySetEqual(response.context["search_results"], Page.objects.none())

        # Check that the search query is present in the response context
        self.assertEqual(response.context["search_query"], search_query)

    def test_site_search_pagination(self):
        # Create more pages to ensure pagination is working
        for i in range(15):
            HomePageFactory(title=f"Test Page {i + 3}", slug=f"test-page-{i + 3}")

        # Create a search query
        search_query = "Test"

        # Simulate a GET request to the search view with a specific page number
        response = self.client.get(reverse("search"), {"query": search_query, "page": 2})

        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, 200)

        # Check that the correct page of search results is present in the response context
        self.assertEqual(response.context["search_results"].number, 2)

    def test_site_search_page_not_an_integer(self):
        # Simulate a GET request to the search view with a non-integer page value
        response = self.client.get(reverse("search"), {"query": "Test", "page": "not_an_integer"})

        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, 200)

        # Check that the search results are from the first page
        self.assertEqual(response.context["search_results"].number, 1)

    def test_site_search_empty_page(self):
        # Create more pages to ensure pagination is working
        for i in range(15):
            HomePageFactory(title=f"Test Page {i + 3}", slug=f"test-page-{i + 3}")

        # Simulate a GET request to the search view with a page number exceeding the available pages
        response = self.client.get(reverse("search"), {"query": "Test", "page": 1000})

        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, 200)

        # Check that the search results are from the last available page
        self.assertEqual(
            response.context["search_results"].number, response.context["search_results"].paginator.num_pages
        )

    def test_site_search_template_used(self):
        # Create a search query
        search_query = "Test"

        # Simulate a GET request to the search view
        response = self.client.get(reverse("search"), {"query": search_query})

        # Check that the correct template is used
        self.assertTemplateUsed(response, "core/search.html")

    def test_site_search_without_query(self):
        # Simulate a GET request to the search view without a search query
        response = self.client.get(reverse("search"))

        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, 200)

        # Check that the search results are an empty queryset
        self.assertQuerySetEqual(response.context["search_results"], Page.objects.none())

        # Check that the search query in the response context is None
        self.assertIsNone(response.context["search_query"])
