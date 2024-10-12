from ..serializers.image import ImageListSerializer
from ..repositories.image import ImageRepository
from src.base.views import generics


class ImageListAPIView(generics.ListAPIView):
    list_serializer_class = ImageListSerializer
    _repository = ImageRepository()
