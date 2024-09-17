from django.urls import path
from .views import (
    CustomSpectacularRedocView,
    CustomSpectacularAPIView,
    CustomSpectacularSwaggerView,
)

urlpatterns = [
    path("schema/", CustomSpectacularAPIView.as_view(), name="schema"),
    path("swagger/", CustomSpectacularSwaggerView.as_view(), name="swagger"),
    path("redoc/", CustomSpectacularRedocView.as_view(), name="redoc"),
]
