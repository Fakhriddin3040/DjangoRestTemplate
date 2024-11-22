from src.apps.product.repositories.product import ProductRepository
from src.apps.product.serializers.product import ProductListSerializer
from src.base.views import generics


class ProductListAPIView(generics.ListAPIView):
    list_serializer_class = ProductListSerializer
    _repository = ProductRepository()
