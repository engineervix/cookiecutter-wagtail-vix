from django.conf import settings
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from wagtail.documents.views import serve
from wagtail.core.models import Page
from wagtail.search.models import Query


def view_document(request, document_id, document_filename):
    """
    Calls the normal document `serve` view, except makes it not an attachment.
    """
    # Get response from `serve` first
    response = serve.serve(request, document_id, document_filename)

    # Remove "attachment" from response's Content-Disposition
    contdisp = response["Content-Disposition"]
    response["Content-Disposition"] = "; ".join(
        [x for x in contdisp.split("; ") if x != "attachment"]
    )

    # Force content-type for pdf files
    if document_filename.split(".")[-1] == "pdf":
        response["Content-Type"] = "application/pdf"

    # Return the response
    return response


def site_search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", request.GET.get("p", 1))
    # page = request.GET.get('page', 1)
    results_per_page = 5
    if search_query:
        search_results = Page.objects.live().search(search_query)
        Query.get(search_query).add_hit()
    else:
        search_query = ""
        search_results = Page.objects.none()
    paginator = Paginator(search_results, results_per_page)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(
        request,
        "base/search_results.html",
        {
            "search_query": search_query,
            "search_results": search_results,
            "title": "{} Search Results for: {}".format(
                settings.WAGTAIL_SITE_NAME, search_query
            ),
        },
    )
