from rest_framework import serializers

from .social_media import SocialMediaListSerializer


class OrganizationListSerializer(serializers.Serializer):
    title = serializers.CharField()
    address = serializers.CharField()
    phone = serializers.CharField()
    phone_two = serializers.CharField()
    email = serializers.CharField()
    social_media = SocialMediaListSerializer(many=True)
    about_us = serializers.CharField()
    coordinates = serializers.CharField()
