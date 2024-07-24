from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.apps.auth.views.user import UserAPIView

from .views import CustomTokenObtainPairView, CustomTokenRefreshView

router = DefaultRouter()

router.register(
    prefix=r"users",
    viewset=UserAPIView,
    basename="users",
)

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
    path("login/refresh/", CustomTokenRefreshView.as_view(), name="refresh-token"),
    path("", include(router.urls)),
]
