from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from src.apps.api import urls as api_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_urls), name="api"),
    path(
        "external/",
        include("src.infrastructure.external_services.moy_sklad.urls"),
        name="external",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
