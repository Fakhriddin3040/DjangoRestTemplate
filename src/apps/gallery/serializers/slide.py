from rest_framework import serializers


class SlideListSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    turn = serializers.IntegerField()
    image = serializers.ImageField(source="image.image")
    link = serializers.CharField()
