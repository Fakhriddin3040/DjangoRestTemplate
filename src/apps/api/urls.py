from django.urls import path, include

from .docs import urls as docs_url
from ..auth import urls as auth_urls

urlpatterns = [
    path("authentication/", include(auth_urls), name="authentication"),
    path(
        "docs/",
        include(docs_url),
        name="docs",
    ),
]
