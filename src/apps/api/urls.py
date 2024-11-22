from django.urls import include, path

from ..auth import urls as auth_urls
from ..gallery import urls as gallery_urls
from ..common import urls as organization_urls
from .docs import urls as docs_url

urlpatterns = [
    path("authentication/", include(auth_urls), name="authentication"),
    path("gallery/", include(gallery_urls), name="gallery"),
    path("common/", include(organization_urls), name="common"),
    path("products/", include("src.apps.product.urls"), name="products"),
    path("categories/", include("src.apps.category.urls"), name="categories"),
    path(
        "docs/",
        include(docs_url),
        name="docs",
    ),
]
