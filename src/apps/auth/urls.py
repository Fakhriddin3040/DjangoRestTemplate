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
    path("users/me", user_views.RetrieveMeAPIView.as_view(), name="get-me"),
    path("profile/", user_views.CreateProfileAPIView.as_view(), name="profile"),
    path(
        "external_services/moy_sklad/products/sync/",
        user_views.ProductSyncAPIView.as_view(),
        name="product-sync",
        ),
    path(
        "external_services/moy_sklad/categories/sync/",
        user_views.CategorySyncAPIView.as_view(),
        name="category-sync"
    )
    
]
