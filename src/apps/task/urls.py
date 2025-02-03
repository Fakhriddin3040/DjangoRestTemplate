from PIL.Image import preinit
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet

router = DefaultRouter()

router.register(
    prefix="",
    viewset=TaskViewSet,
    basename="todo"
)

urlpatterns = [
    path("", include(router.urls))
]