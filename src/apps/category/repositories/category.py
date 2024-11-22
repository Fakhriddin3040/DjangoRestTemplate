from src.apps.category.models.category import Category
from src.base.abstractions.repositories import base_django_repository


class CategoryRepository(base_django_repository.AbstractDjangoRepository[Category]):
    model = Category
