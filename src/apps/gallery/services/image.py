from typing import Union
import requests
from src.apps.gallery.functions import save_image
from src.apps.gallery.repositories import image as image_repositories
from src.base.abstractions.repositories.base_django_repository import (
    AbstractDjangoRepository,
)
from src.apps.gallery import const as gallery_const
from ..models.image import Image
from src.base.abstractions.services.base_service import AbstractService


class ImageService(AbstractService[Image]):
    def __init__(self, repository: AbstractDjangoRepository[Image] = None) -> None:
        super().__init__(repository or image_repositories.ImageRepository())

    def upload_image(
        self, image: Union[int, Image], ext: str = None, **request_kwargs
    ) -> Image:
        if isinstance(image, int):
            image = self.get_by_id(image)

        ext = ext or gallery_const.DEFAULT_IMG_EXT

        response = requests.get(image.url, **request_kwargs)
        response.raise_for_status()
        filename = f"{image.id}.{ext}"
        image_path = save_image(
            response.content, gallery_const.PRODUCT_IMAGES_PATH, filename=filename
        )
        image.image = image_path
        image.save()
        return image
