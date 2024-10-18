from django.urls import path
from .views import slide

urlpatterns = [
    path(r"slides/", slide.SlideListAPIView.as_view()),
]
