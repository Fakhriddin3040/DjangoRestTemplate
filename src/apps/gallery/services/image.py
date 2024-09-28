from src.apps.gallery.repositories.image import ImageRepository
from src.base.abstractions.repositories.base_django_repository import (
    AbstractDjangoRepository,
)
from ..models.image import Image
from src.base.abstractions.services.base_service import AbstractService


class ImageService(AbstractService[Image]):
    def __init__(self, repository: AbstractDjangoRepository) -> None:
        super().__init__(repository or ImageRepository())
