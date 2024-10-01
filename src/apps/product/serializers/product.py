from rest_framework import serializers


class ProductListSerializer(serializers.Serializer):
    identifier = serializers.CharField()


class ProductCreateSerializer(serializers.Serializer):
    identifier = serializers.CharField()
