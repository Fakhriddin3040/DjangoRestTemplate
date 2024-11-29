from typing import Any, Dict
from src.infrastructure.external_services.moy_sklad.mappers.base import MKBaseMapper
from .. import const as moy_sklad_const


class MKImageMapper(MKBaseMapper):
    def __init__(self, map=None):
        super().__init__(
            map or moy_sklad_const.IMAGE_FIELD_MAP,
        )

    def get_image_id(self, data: Dict[str, Any], key: str) -> str:
        value = data.get(key)
        return value.split("/")[-1] if value else None
