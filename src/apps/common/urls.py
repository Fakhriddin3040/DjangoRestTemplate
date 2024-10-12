from django.urls import path
from .views.organization import OrganizationListAPIView


urlpatterns = [
    path("organization/", OrganizationListAPIView.as_view(), name="organization"),
]
