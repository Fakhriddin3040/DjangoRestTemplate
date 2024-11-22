# from typing import Dict
# from ..models import Product
# from src.utils.mapping import field_mapper
# from ..services import product as product_services


# # class ProductSyncService:
# #     model = Product
# #     map: Dict[str, str] =

# #     def __init__(
# #         self,
# #         product_service: product_services.ProductService = None,
# #     ) -> None:
# #         self.mapper = mapper or field_mapper.FieldMapper()
# #         self.product_service = product_service or product_services.ProductService()

# #     def sync_product(self, data: Dict) -> None:
# #         mapped_data = self.mapper.map_fields(data)
# #         return self.product_service.create_or_update(**mapped_data)

# #     def sync_products(self, data: Dict) -> None:
# #         for product in data:
# #             self.sync_product(product)
