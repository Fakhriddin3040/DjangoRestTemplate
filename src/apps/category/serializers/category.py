from rest_framework import serializers

from src.apps.category.models.category import Category


class CategoryListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    ext_id = serializers.CharField()
    title = serializers.CharField()
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), required=False
    )
