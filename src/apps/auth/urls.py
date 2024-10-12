from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.apps.auth.views import user as user_views

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("login/", user_views.UserLoginAPIView.as_view()),
    path("registration/phone/1/", user_views.UserPhoneStep2RegisterAPIView.as_view()),
    path("registration/phone/2/", user_views.UserPhoneStep1RegisterAPIView.as_view()),
    path("registration/phone/3/, user_views.UserPhoneStep3RegisterAPIView.as_view()),
    path(
        "registration/email/1/", user_views.UserEmailStep1RegisterAPIView.as_view()
    ),
    path(
        "registration/email/2/",  user_views.UserEmailStep2RegisterAPIView.as_view()
    ),
    path(
        "registration/email/3/", user_views.UserEmailStep3RegisterAPIView.as_view()
    ),
    path("registration/oauth2/", user_views.UserOAuthRegisterAPIView.as_view()),
    path("login/oauth2/", user_views.UserOAuthLoginAPIView.as_view()),
]
