from ..serializers.slide import SlideListSerializer
from ..repositories.slide import SlideRepository

from src.base.views import generics


class SlideListAPIView(generics.ListAPIView):
    list_serializer_class = SlideListSerializer
    _repository = SlideRepository()
