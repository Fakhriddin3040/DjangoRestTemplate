from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.apps.auth.views import user as user_views

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("login/", user_views.UserLoginAPIView.as_view()),
    path("registration/phone/", user_views.PhoneRegistrationAPIView.as_view()),
    path("registration/email/", user_views.UserEmailStep1RegisterAPIView.as_view()),
    path(
        "registration/credentials-verification/",
        user_views.CredentialsVerificationAPIView.as_view(),
        name="credentials-verification",
    ),
    path(
        "registration/finish/",
        user_views.RegistrationFinishAPIView.as_view(),
        name="registration-finish",
    ),
    path("oauth2/", user_views.OAuthAPIView.as_view(), name="oauth2"),
]
