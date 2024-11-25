import datetime
from src.base.abstractions.services import base_service

from ..repositories import mk_sync_info as mk_sync_info_repos
from ..models import mk_sync_info as mk_sync_info_model


class MKSyncInfoService(base_service.AbstractService[mk_sync_info_model.MKSyncInfo]):
    def __init__(self, repository: mk_sync_info_repos.MKSyncInfoRepository):
        super().__init__(repository or mk_sync_info_repos.MKSyncInfoRepository())

    def get_latest_product_synced(self) -> datetime.datetime:
        return self._repository.get_latest_product_synced().prod_synced

    def get_latest_category_synced(self) -> datetime.datetime:
        return self._repository.get_latest_category_synced().cat_synced

    def get_latest_synced(self) -> datetime.datetime:
        return self._repository.get_latest_synced().synced
