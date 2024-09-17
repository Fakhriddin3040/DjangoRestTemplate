from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.apps.auth.views import user as user_views

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("login/", user_views.UserLoginAPIView.as_view()),
    path("register/", user_views.UserRegisterAPIView.as_view()),
]
