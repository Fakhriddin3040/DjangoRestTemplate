from django.urls import path

from src.apps.category.views.category import CategoryListAPIView


urlpatterns = [
    path("", CategoryListAPIView.as_view(), name="category-list"),
]
