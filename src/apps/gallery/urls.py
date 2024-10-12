from django.urls import path


from .views import image, slide


urlpatterns = [
    path(r"images/", image.ImageListAPIView.as_view()),
    path(r"slides/", slide.SlideListAPIView.as_view()),
]
