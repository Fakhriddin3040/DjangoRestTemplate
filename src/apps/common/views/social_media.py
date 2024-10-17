from src.apps.common.repositories.social_media import SocialMediaRepository
from src.apps.common.serializers.social_media import SocialMediaListSerializer
from src.base.views import generics


class SocialMediaListAPIView(generics.ListAPIView):
    _repository = SocialMediaRepository()
    list_serializer_class = SocialMediaListSerializer