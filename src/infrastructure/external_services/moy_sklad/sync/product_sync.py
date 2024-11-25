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
    def __init__(self, parser=None, api=None, service=None) -> None:
        super().__init__(
            parser=parser or MKProductParser(),
            api=api or MKProductAPI(api_key=moy_sklad_const.API_KEY),
            service=service or MKSyncInfoService(),
        )
        self.image_parser = MKImageParser()

    def _sync(self, data: List[Dict[str, Any]]) -> int:
        for item in data:
            self._set_images(item)
        return super()._sync(data)

    def _set_images(self, data: Dict[str, Any]) -> None:
        images_endpoint = data.get("images_endpoint")
        if not images_endpoint:
            return

        images_data = self.api.get(endpoint=images_endpoint).json

        for item in images_data:
            image = self.image_parser.parse_entity(item)
            self.image_parser.service.upload_image(image, self.api.get_headers())
