from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.apps.auth.views import user as user_views

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("login/", user_views.UserLoginAPIView.as_view()),
    path("register/", user_views.UserRegisterAPIView.as_view()),
    path("phone_register/step1", user_views.UserPhoneStep1RegisterAPIView.as_view()),
    path("phone_register/step2", user_views.UserPhoneStep2RegisterAPIView.as_view()),
    path("phone_register/step3", user_views.UserPhoneStep3RegisterAPIView.as_view()),
    path("email_registration/step1", user_views.UserEmailStep1RegisterAPIView.as_view()),
    path("email_registration/step2", user_views.UserEmailStep2RegisterAPIView.as_view()),
    path("email_registration/step3", user_views.UserEmailStep3RegisterAPIView.as_view()),
    path("oauth-register/", user_views.UserOAuthRegisterAPIView.as_view()),
    path("oauth-login/", user_views.UserOAuthLoginAPIView.as_view()),
]
