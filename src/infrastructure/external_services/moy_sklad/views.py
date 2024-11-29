from rest_framework import views, status
from rest_framework.response import Response
from .sync import category as category_sync, product as product_sync


class ProductSyncAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        sync = product_sync.ProductSyncService()
        created_count, data_len = sync.sync()
        data = {"created": created_count, "data_len": data_len}
        return Response(data, status=status.HTTP_200_OK)


class CategorySyncAPIView(views.APIView):
    def post(self, request, *args, **kwargs) -> Response:
        sync = category_sync.CategorySyncService()
        orders = ["pathName__desc"]
        created_count, data_len = sync.sync(orders=orders)
        data = {"created": created_count, "data_len": data_len}
        return Response(data, status=status.HTTP_200_OK)
