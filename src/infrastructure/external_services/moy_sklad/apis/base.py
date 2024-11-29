import datetime
from typing import Any, Dict, List

from src.infrastructure.external_services.moy_sklad.functions import (
    datetime_to_moy_sklad_format,
)
from src.infrastructure.external_services.moy_sklad.services.mk_sync_info import (
    MKSyncInfoService,
)
from src.utils.functions.functions import (
    set_timezone_info,
    datetime_from_moy_sklad_format,
)
from .. import const as moy_sklad_const
from src.infrastructure.base import api_client as base_api_client


class MKModelAPIBase(base_api_client.BaseApiClient):
    HOST = moy_sklad_const.HOST
    ORDERS_MAP = moy_sklad_const.ORDERS_LOOKUP_MAP
    FILTERS_MAP = moy_sklad_const.FILTERS_LOOKUP_MAP

    def __init__(self, api_key: str = None) -> None:
        super().__init__(api_key or moy_sklad_const.API_KEY)
        self.service = MKSyncInfoService()

    def fetch_updated_objects(
        self, updated: datetime.datetime, **kwargs
    ) -> List[Dict[str, Any]]:
        formatted_datetime = datetime_to_moy_sklad_format(updated)
        filters = {"updated__gt": formatted_datetime}

        return self.fetch_objects(filters=filters)

    def fetch_null_ordered(self, field: str) -> List[Dict[str, Any]]:
        orders = [f"{field}__isnull"]

        return self.fetch_objects(orders=orders)

    def get_latest_updated(self) -> datetime.datetime:
        str_dt = self.fetch_objects(orders=["updated__desc"], params={"limit": 1})[0][
            "updated"
        ]
        dt_naive = datetime_from_moy_sklad_format(str_dt)
        return set_timezone_info(dt_naive)

    def get_rows(self, response):
        return response.json()["rows"]
