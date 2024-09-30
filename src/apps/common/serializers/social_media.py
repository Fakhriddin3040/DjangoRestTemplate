from rest_framework import serializers


class SocialMediaListSerializer(serializers.Serializer):
    title = serializers.CharField()
    link = serializers.CharField()
    icon = serializers.ImageField()
