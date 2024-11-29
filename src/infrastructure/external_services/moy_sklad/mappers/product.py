from typing import Any, Dict
from .base import MKBaseMapper
from .. import const as moy_sklad_const


class MKProductMapper(MKBaseMapper):
    def get_product_folder_ext_id(self, data: Dict[str, str], key: str):
        value = data.get(key)
        return value.split("/")[-1] if value is not None else None

    def get_sell_price(self, data: Dict[str, str], key: str):
        return data[0].get(key)

    def get_images_endpoint(self, data: Dict[str, Any], key: str) -> str:
        value: str = data.get(key)
        return value.removeprefix(f"{moy_sklad_const.HOST}/")
