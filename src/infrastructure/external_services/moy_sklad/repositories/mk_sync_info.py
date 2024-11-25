from src.base.abstractions.repositories import base_django_repository

from ..models import mk_sync_info as mk_sync_info_model


class MKSyncInfoRepository(
    base_django_repository.AbstractDjangoRepository[mk_sync_info_model.MKSyncInfo]
):
    model = mk_sync_info_model.MKSyncInfo

    def get_latest_product_synced(self) -> mk_sync_info_model.MKSyncInfo:
        return self.model.objects.latest("prod_synced")

    def get_latest_category_synced(self) -> mk_sync_info_model.MKSyncInfo:
        return self.model.objects.latest("cat_synced")

    def get_latest_synced(self) -> mk_sync_info_model.MKSyncInfo:
        return self.model.objects.latest("synced")
