from src.apps.product.models.product import Product
from src.apps.product.params.product import ProductCreateParams, ProductUpdateParams
from src.base.abstractions.services.base_service import AbstractService
from ..services import ProductService


class ProductCreateUseCase:
    def __init__(self, product_service: AbstractService = None) -> None:
        self.product_service = product_service or ProductService()

    def execute(self, params: ProductCreateParams) -> Product:
        product = self.product_service.create(params=params)
        return product


class ProductUpdateUseCase:
    def __init__(self, product_service: AbstractService = None) -> None:
        self.product_service = product_service or ProductService()

    def execute(self, pk: int, params: ProductUpdateParams) -> Product:
        result = self.product_service.update(pk=pk, params=params)
        if result != 1:
            raise Exception("Ошибка при обновлении продукта")
        product = self.product_service.get(pk=pk)
        return product
