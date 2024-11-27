from django_filters import FilterSet, filters

from src.apps.product.models.product import Product

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = (
            "category_id",
        )
    price = filters.NumericRangeFilter()