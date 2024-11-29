from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple, Union
from src.base.abstractions.services.base_service import AbstractService
from src.infrastructure.external_services.moy_sklad.parsers.base import MKParserBase

from ..apis import base as api_base


class MKSyncBase:
    def __init__(
        self,
        parser: MKParserBase,
        api: api_base.MKModelAPIBase,
        sync_info_service: AbstractService,
    ) -> None:
        self.parser = parser
        self.api = api
        self.sync_info_service = sync_info_service

    @property
    def model_service(self) -> AbstractService:
        return self.parser.model_service

    def fetch_objects(self, *args, **kwargs) -> List[Dict[str, Any]]:
        return self.api.fetch_objects(*args, **kwargs)

    def sync(self, force: bool = False, *args, **kwargs) -> Tuple[int, int]:
        if force:
            data = self.api.fetch_objects(*args, **kwargs)
        else:
            synced_times = self.last_synced_at()
            need_sync = self.need_sync(*synced_times)

            if not need_sync:
                return 0, 0

            last_updated = self.sync_info_service.get_latest_synced()

            if not last_updated:
                data = self.api.fetch_objects(*args, **kwargs)
            else:
                data = self.api.fetch_updated_objects(last_updated, *args, **kwargs)

        self._ensure_data_type(data)

        data_len = len(data)
        created_count = self._sync(data)

        self.save_sync_info()

        return created_count, data_len

    def _sync(self, data: List[Dict[str, Any]]) -> int:
        return self.parser.map_and_parse_entities(data)

    def _ensure_data_type(self, data: Any):
        if not isinstance(data, list) and all(isinstance(item, dict) for item in data):
            raise ValueError("Data must be a list of dictionaries")

    def last_synced_at(self) -> Union[Tuple[datetime, datetime], None]:
        local_updated = self.sync_info_service.get_latest_synced()
        remote_updated = self.api.get_latest_updated()

        return local_updated, remote_updated

    def need_sync(
        self,
        local_updated: Optional[datetime] = None,
        remote_updated: Optional[datetime] = None,
    ) -> bool:
        return (
            local_updated is None and remote_updated
        ) or remote_updated > local_updated

    def save_sync_info(self):
        self.sync_info_service.save_sync_info(self.api.get_latest_updated())
