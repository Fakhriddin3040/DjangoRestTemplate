from src.infrastructure.external_services.moy_sklad.parsers.base import MKParserBase
from src.infrastructure.external_services.moy_sklad.sync.base import MKSyncBase
from src.infrastructure.external_services.moy_sklad.parsers.product import (
    MKProductParser,
)


class ProductSyncService(MKSyncBase):
    def __init__(self, parser: MKParserBase = None):
        super().__init__(parser=parser or MKProductParser())
