from rest_framework import serializers

from src.apps.common.models.social_media import SocialMedia


class SocialMediaListSerializer(serializers.Serializer):
    link = serializers.CharField()
    icon = serializers.ImageField()
    social_type = serializers.ChoiceField(choices=SocialMedia.SOCIAL_MEDIA_CHOICES)
