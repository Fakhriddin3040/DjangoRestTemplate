from django.urls import path
from . import views as moy_sklad_views

urlpatterns = [
    path(
        "external_services/moy_sklad/products/sync/",
        moy_sklad_views.ProductSyncAPIView.as_view(),
        name="product-sync",
    ),
    path(
        "external_services/moy_sklad/categories/sync/",
        moy_sklad_views.CategorySyncAPIView.as_view(),
        name="category-sync",
    ),
]
