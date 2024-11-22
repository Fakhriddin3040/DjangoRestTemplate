from src.infrastructure.external_services.moy_sklad.parsers.category import (
    MKCategoryParser,
)
from src.infrastructure.external_services.moy_sklad.sync.base import MKSyncBase


class CategorySyncService(MKSyncBase):
    def __init__(self, parser=None):
        super().__init__(parser or MKCategoryParser())
