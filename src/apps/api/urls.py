from django.urls import include, path

from ..auth import urls as auth_urls
from ..gallery import urls as gallery_urls
from .docs import urls as docs_url

urlpatterns = [
    path("authentication/", include(auth_urls), name="authentication"),
    path("gallery/", include(gallery_urls), name="gallery"),
    path(
        "docs/",
        include(docs_url),
        name="docs",
    ),
]
