from typing import Union
import requests
from src.apps.gallery.functions import save_image
from src.apps.gallery.repositories import image as image_repositories
from src.base.abstractions.repositories.base_django_repository import (
    AbstractDjangoRepository,
)
from ..models.image import Image
from src.base.abstractions.services.base_service import AbstractService


class ImageService(AbstractService[Image]):
    def __init__(self, repository: AbstractDjangoRepository[Image]) -> None:
        super().__init__(repository or image_repositories.ImageRepository())

    def upload_image(self, image: Union[int, Image], **request_kwargs) -> Image:
        if isinstance(image, int):
            image = self.get_by_id(image)

        response = requests.get(image.url, **request_kwargs)
        response.raise_for_status()
        filename = image.url.split("/")[-1]
        image_path = save_image(response.content, filename=filename)
        image.image = image_path
        image.save()
        return image
