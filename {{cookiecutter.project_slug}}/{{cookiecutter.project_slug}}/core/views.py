from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from wagtail.contrib.search_promotions.models import Query
from wagtail.models import Page


def site_search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", request.GET.get("p", 1))

    # Search
    if search_query:
        search_results = Page.objects.live().search(search_query)
        # Log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    results_per_page = 12
    paginator = Paginator(search_results, results_per_page)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "core/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
            "title": "{} Search Results for: {}".format(settings.WAGTAIL_SITE_NAME, search_query),
        },
    )
