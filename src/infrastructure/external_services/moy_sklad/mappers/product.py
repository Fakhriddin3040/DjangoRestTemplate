from typing import Dict
from .base import MKBaseMapper


class MKProductMapper(MKBaseMapper):
    def get_product_folder_ext_id(self, data: Dict[str, str], key: str):
        value = data.get(key)
        return value.split("/")[-1] if value is not None else None

    def get_sell_price(self, data: Dict[str, str], key: str):
        return data[0].get(key)
