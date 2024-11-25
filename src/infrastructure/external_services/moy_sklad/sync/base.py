from typing import Any, Dict, List, Tuple
from src.infrastructure.external_services.moy_sklad.parsers.base import MKParserBase
from src.infrastructure.external_services.moy_sklad.services.mk_sync_info import (
    MKSyncInfoService,
)

from ..apis import base as api_base


class MKSyncBase:
    def __init__(
        self,
        parser: MKParserBase,
        api: api_base.MKModelAPIBase,
        service: MKSyncInfoService,
    ) -> None:
        self.parser = parser
        self.api = api
        self.service = service

    def fetch_objects(self, *args, **kwargs) -> List[Dict[str, Any]]:
        return self.api.fetch_objects(*args, **kwargs)

    def sync(self, force: bool = False, *args, **kwargs) -> Tuple[int, int]:
        need_sync = self.need_sync()

        if not force and not need_sync:
            return 0, 0

        if need_sync:
            data = self.api.fetch_updated_objects(*args, **kwargs)
        elif force:
            data = self.api.fetch_objects(*args, **kwargs)

        self._ensure_data_type(data)

        data_len = len(data)
        created_count = self._sync(data)

        return created_count, data_len

    def _sync(self, data: List[Dict[str, Any]]) -> int:
        return self.parser.parse_entities(data)

    def _ensure_data_type(self, data: Any):
        if not isinstance(data, list) and all(isinstance(item, dict) for item in data):
            raise ValueError("Data must be a list of dictionaries")

    def need_sync(self) -> bool:
        return self.service.get_last_synced() >= self.api.get_latest_updated()
