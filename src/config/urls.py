from django.contrib import admin
from django.urls import include, path

from src.apps.api import urls as api_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_urls), name="api"),
]
