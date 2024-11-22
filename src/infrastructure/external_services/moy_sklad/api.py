import datetime
from typing import Dict, Optional

from src.infrastructure.external_services.moy_sklad.functions import (
    datetime_to_moy_sklad_format,
)
from . import const as moy_sklad_const
from src.infrastructure.base import api_client as base_api_client


class MoySkladAPI(base_api_client.BaseApiClient):
    BASE_URL = moy_sklad_const.BASE_URL
    FILTERS_MAP = moy_sklad_const.LOOKUP_MAP
    OBJECTS_PATH = moy_sklad_const.ENTITY_PATH
    PRODUCT_FOLDER_PATH = "productfolder"
    PRODUCT_PATH = "product"

    def get_prod_folders(
        self,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, str]] = None,
        filters: Optional[Dict[str, str]] = None,
        orders: Optional[Dict[str, str]] = None,
        **kwargs,
    ) -> Dict[str, str]:
        return self.fetch_objects(
            entity_url=self.PRODUCT_FOLDER_PATH,
            headers=headers,
            params=params,
            filters=filters,
            orders=orders,
            **kwargs,
        )

    def get_updated_prod_folders(
        self,
        headers: Optional[Dict[str, str]],
        params: Optional[Dict[str, str]],
        filters: Optional[Dict[str, str]],
        orders: Optional[Dict[str, str]],
        updated: datetime.datetime,
        **kwargs,
    ) -> Dict[str, str]:
        ms_formatted_updated = datetime_to_moy_sklad_format(updated)

        return self.fetch_objects(
            entity_url=self.PRODUCT_FOLDER_PATH,
            headers=headers,
            params=params,
            updated__gt=ms_formatted_updated,
            filters=filters,
            orders=orders,
            **kwargs,
        )

    def get_products(
        self,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, str]] = None,
        orders: Optional[Dict[str, str]] = None,
        filters: Optional[Dict[str, str]] = None,
        **kwargs,
    ) -> Dict[str, str]:
        return self.fetch_objects(
            entity_url=self.PRODUCT_PATH,
            headers=headers,
            params=params,
            orders=orders,
            filters=filters,
            **kwargs,
        )

    def get_updated_products(
        self,
        headers: Optional[Dict[str, str]],
        params: Optional[Dict[str, str]],
        updated: datetime.datetime,
        orders: Optional[Dict[str, str]],
        filters: Optional[Dict[str, str]],
        **kwargs,
    ) -> Dict[str, str]:
        ms_formatted_updated = datetime_to_moy_sklad_format(updated)
        return self.fetch_objects(
            entity_url=self.PRODUCT_PATH,
            headers=headers,
            params=params,
            filters=filters,
            orders=orders,
            updated__gt=ms_formatted_updated,
            **filters,
        )
