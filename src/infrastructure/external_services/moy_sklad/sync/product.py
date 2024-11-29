from typing import Any, Dict, List
from src.infrastructure.external_services.moy_sklad.apis.product import MKProductAPI
from src.infrastructure.external_services.moy_sklad.parsers.image import MKImageParser
from src.infrastructure.external_services.moy_sklad.services.mk_sync_info import (
    MKSyncInfoService,
)
from src.infrastructure.external_services.moy_sklad.sync.base import MKSyncBase
from src.infrastructure.external_services.moy_sklad.parsers.product import (
    MKProductParser,
)

from .. import const as moy_sklad_const


class ProductSyncService(MKSyncBase):
    def __init__(self, parser=None, api=None, sync_info_service=None) -> None:
        super().__init__(
            parser=parser or MKProductParser(),
            api=api or MKProductAPI(api_key=moy_sklad_const.API_KEY),
            sync_info_service=sync_info_service or MKSyncInfoService(),
        )
        self.image_parser = MKImageParser()

    def _sync(self, data: List[Dict[str, Any]]) -> int:
        created_count = 0

        for item in data:
            parsed_data = self.parser.map_data(item)
            images_endpoint = parsed_data.pop("images_endpoint")
            images = self._set_images(images_endpoint, item)
            instance, created = self.parser.parse_entity(parsed_data)
            instance.images.set(images)
            instance.save()
            created_count += created

        return created_count

    def _set_images(self, images_endpoint: str, data: Dict[str, Any]) -> None:
        if not images_endpoint:
            return

        images_data = self.api.get_rows(self.api.get(endpoint=images_endpoint))
        images = []

        for item in images_data:
            image, _ = self.image_parser.map_and_parse_entity(item)
            images.append(
                self.image_parser.model_service.upload_image(
                    image=image,
                    ext=moy_sklad_const.PRODUCT_IMAGE_FORMAT,
                    headers=self.api.get_headers(),
                )
            )
        return images
