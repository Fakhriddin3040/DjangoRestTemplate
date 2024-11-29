from src.base.abstractions.repositories import base_django_repository

from ..models.image import Image


class ImageRepository(base_django_repository.AbstractDjangoRepository[Image]):
    model = Image
