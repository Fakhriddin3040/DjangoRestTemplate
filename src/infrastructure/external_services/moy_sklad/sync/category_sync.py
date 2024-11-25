from src.apps.category.services.category import CategoryService
from src.infrastructure.external_services.moy_sklad.apis.category import MKCategoryAPI
from src.infrastructure.external_services.moy_sklad.parsers.category import (
    MKCategoryParser,
)
from src.infrastructure.external_services.moy_sklad.sync.base import MKSyncBase
from .. import const as moy_sklad_const


class CategorySyncService(MKSyncBase):
    def __init__(self, parser=None):
        super().__init__(
            parser or MKCategoryParser(),
            api=MKCategoryAPI(
                api_key=moy_sklad_const.API_KEY,
            ),
            service=CategoryService()
            )
