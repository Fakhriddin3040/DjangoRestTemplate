from ..serializers.slide import SlideListSerializer
from ..repositories.slide import SlideRepository

from src.base.views import local_generics


class SlideListAPIView(local_generics.ListAPIView):
    list_serializer_class = SlideListSerializer
    _repository = SlideRepository()
