from typing import Union
from src.base.abstractions.repositories import base_django_repository

from ..models import mk_sync_info as mk_sync_info_model


class MKSyncInfoRepository(
    base_django_repository.AbstractDjangoRepository[mk_sync_info_model.MKSyncInfo]
):
    model = mk_sync_info_model.MKSyncInfo

    def get_by_latest_product_synced(
        self,
    ) -> Union[mk_sync_info_model.MKSyncInfo, None]:
        return self.model.objects.order_by("prod_synced_at").first()

    def get_by_latest_category_synced(
        self,
    ) -> Union[mk_sync_info_model.MKSyncInfo, None]:
        return self.model.objects.order_by("cat_synced_at").first()

    def get_by_latest_synced(self) -> Union[mk_sync_info_model.MKSyncInfo, None]:
        return self.model.objects.order_by("synced_at").first()
