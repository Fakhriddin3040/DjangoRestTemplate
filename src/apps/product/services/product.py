from src.apps.product.functions import validate_product_field_uniquness
from src.base import types
from src.apps.product.models.product import Product
from src.base.abstractions.repositories.base_django_repository import (
    AbstractDjangoRepository,
)
from src.base.abstractions.services.base_service import AbstractService

from ..repositories import ProductRepository


class ProductService(AbstractService[Product]):
    def __init__(self, repository: AbstractDjangoRepository = None) -> None:
        super().__init__(repository or ProductRepository())

    def create(self, params: types.BaseParams) -> Product:
        validate_product_field_uniquness(
            field="title",
            value=params.title,
            product_service=self,
        )
        return super().create(params)

    def update(self, pk: int, params: types.BaseParams) -> int:
        validate_product_field_uniquness(
            field="title",
            value=params.title,
            product_service=self,
            exclude={"pk": pk},
        )
        return super().update(pk=pk, params=params)
