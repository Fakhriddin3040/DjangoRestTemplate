from ..models.image import Image
from src.base.abstractions.repositories.base_django_repository import (
    AbstractDjangoRepository,
)


class ImageRepository(AbstractDjangoRepository[Image]):
    model = Image
