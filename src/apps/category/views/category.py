from src.apps.category.repositories.category import CategoryRepository
from src.apps.category.serializers.category import CategoryListSerializer
from src.base.views import local_generics


class CategoryListAPIView(local_generics.ListAPIView):
    list_serializer_class = CategoryListSerializer
    _repository = CategoryRepository()
