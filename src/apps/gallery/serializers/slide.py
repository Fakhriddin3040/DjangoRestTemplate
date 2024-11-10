from rest_framework import serializers


class SlideListSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    image = serializers.ImageField()
    link = serializers.CharField()
