from rest_framework import serializers
from ..models import Slide


class SlideListSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    image = serializers.ImageField()
    link = serializers.CharField()
