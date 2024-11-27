from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework import views
from rest_framework import viewsets
from src.apps.product.filters.product import ProductFilter
from src.apps.product.repositories.product import ProductRepository
from src.apps.product.serializers.product import ProductListSerializer
from src.base.views import local_generics

views.APIView
class ProductListAPIView(local_generics.ListAPIView):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    list_serializer_class = ProductListSerializer
    _repository = ProductRepository()

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="category_id",
                type=OpenApiTypes.INT,
                required=False,
                description="pdsytiosf"
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Создаем экземпляр ProductFilter и передаем запрос #TODO
        filterset = ProductFilter(self.request.GET, queryset=queryset)

        # Проверяем, валидны ли фильтры
        if not filterset.is_valid():
            raise Exception(filterset.errors)
        
        # Применяем фильтрацию
        return filterset.qs