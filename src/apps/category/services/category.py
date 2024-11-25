from src.apps.category.models.category import Category
from src.apps.category.repositories import category as category_repository
from src.base.abstractions.services import base_service
from src.base.abstractions.repositories import base_django_repository


class CategoryService(base_service.AbstractService[Category]):
    def __init__(
        self, repository: base_django_repository.AbstractDjangoRepository = None
    ) -> None:
        super().__init__(
            repository=repository or category_repository.CategoryRepository()
        )

    def get_last_synced(self) 
