from rest_framework import serializers


class OrganizationListSerializer(serializers.Serializer):
    title = serializers.CharField()
    address = serializers.CharField()
    phone = serializers.CharField()
    icon = serializers.ImageField()
    phone_two = serializers.CharField()
    email = serializers.CharField()
    about_us = serializers.CharField()
    coordinates = serializers.CharField()
