from django.urls import path

from src.apps.common.views.social_media import SocialMediaListAPIView
from .views.organization import OrganizationListAPIView


urlpatterns = [
    path("organization/", OrganizationListAPIView.as_view(), name="organization"),
    path("social-media/", SocialMediaListAPIView.as_view(), name="get_social_media"),
]
