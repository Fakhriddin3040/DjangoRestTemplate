from rest_framework import serializers


class ImageListSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.ImageField()
    url = serializers.CharField()
