from src.base.abstractions.repositories.base_django_repository import (
    AbstractDjangoRepository,
)

from ..models import Product


class ProductRepository(AbstractDjangoRepository[Product]):
    model = Product
