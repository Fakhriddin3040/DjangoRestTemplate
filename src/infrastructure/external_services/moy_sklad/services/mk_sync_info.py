import datetime
from typing import Optional, Union
from src.base.abstractions.services import base_service
from ..params import mk_sync_info as mk_sync_info_params
from ..repositories import mk_sync_info as mk_sync_info_repos
from ..models import mk_sync_info as mk_sync_info_model


class MKSyncInfoService(base_service.AbstractService[mk_sync_info_model.MKSyncInfo]):
    def __init__(
        self, repository: Optional[mk_sync_info_repos.MKSyncInfoRepository] = None
    ):
        super().__init__(repository or mk_sync_info_repos.MKSyncInfoRepository())

    def get_latest_product_synced(self) -> Union[datetime.datetime, None]:
        result = self._repository.get_by_latest_product_synced()
        return result.prod_synced_at if result else None

    def get_latest_category_synced(self) -> Union[datetime.datetime, None]:
        result = self._repository.get_by_latest_category_synced()
        return result.cat_synced_at if result else None

    def get_latest_synced(self) -> Union[datetime.datetime, None]:
        result = self._repository.get_by_latest_synced()
        return result.synced_at if result else None

    def save_sync_info(self, synced_at: datetime.datetime) -> None:
        params = mk_sync_info_params.MKSyncInfoCreateParams(
            synced_at=synced_at,
        )
        self.create(params=params)
