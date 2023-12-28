from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.documents import urls as wagtaildocs_urls

from {{cookiecutter.project_slug}}.core.views import site_search

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", site_search, name="search"),
    re_path(r"^sitemap\.xml$", sitemap),
    # Django-RQ
    # path("dj-rq/", include("django_rq.urls")),
]


if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
