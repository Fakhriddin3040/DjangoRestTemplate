from typing import List

from src.infrastructure.external_services.moy_sklad.sync.base import MKSyncBase
from . import product
from . import category
from ..apis.base import MKModelAPIBase


class MKSync:
    def __init__(self) -> None:
        self.syncs_classes: List[MKSyncBase] = [
            product.ProductSyncService(),
            category.CategorySyncService(),
        ]
        api_key = "9903b4458420aa193f41d12c6c7205f8324a4f0f"
        self.api = MKModelAPIBase(api_key)

    def sync(self):
        data = self.api.get_prod_folders()
        self.syncs_classes[1].sync(data=data["rows"])
        data = self.api.get_products()
        self.syncs_classes[0].sync(data=data["rows"])

    def sync_class(self, sync_class):
        data = self.api.get_products()
        sync_class.sync(data=data["rows"])
