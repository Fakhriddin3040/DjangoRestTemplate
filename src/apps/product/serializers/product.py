from rest_framework import serializers
from src.apps.category.models import Category


class ProductBaseSerializer(serializers.Serializer):
    ext_id = serializers.CharField()
    ext_cat_id = serializers.CharField(required=False, allow_null=True)
    title = serializers.CharField()
    description = serializers.CharField(required=False, allow_null=True)
    price = serializers.DecimalField(
        max_digits=10, decimal_places=2, required=False, allow_null=True
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), required=False, allow_null=True
    )
    on_sale = serializers.BooleanField()
    discount = serializers.DecimalField(
        max_digits=10, decimal_places=2, required=False, allow_null=True
    )
    count = serializers.IntegerField(default=0)
    weight = serializers.DecimalField(
        max_digits=10, decimal_places=2, required=False, allow_null=True
    )
    brand = serializers.CharField(required=False, allow_null=True)
    model = serializers.JSONField(required=False, allow_null=True)
    colors = serializers.JSONField(required=False, allow_null=True)
    vendor_code = serializers.CharField(required=False, allow_null=True)
    production_year = serializers.IntegerField(required=False, allow_null=True)


class ProductListSerializer(ProductBaseSerializer):
    id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class ProductCreateSerializer(ProductBaseSerializer):
    pass
