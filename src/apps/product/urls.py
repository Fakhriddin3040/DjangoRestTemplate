from django.urls import path

from src.apps.product.views.product import ProductListAPIView

urlpatterns = [
    path("", ProductListAPIView.as_view(), name="product-list"),
]
