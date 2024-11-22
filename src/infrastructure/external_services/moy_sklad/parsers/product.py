from src.apps.product.services import product as product_services
from src.apps.category.services import category as category_services
from src.base.abstractions.services import base_service
from src.infrastructure.external_services.moy_sklad.mappers.product import (
    MKProductMapper,
)
from src.utils.mapping.field_mapper import FieldMapper
from .base import MKParserBase
from .. import const


class MKProductParser(MKParserBase):
    def __init__(
        self,
        mapper: FieldMapper = None,
        service: base_service.AbstractService = None,
        category_service: base_service.AbstractService = None,
    ):
        self.mapper = mapper or MKProductMapper(const.MK_PRODUCT_FIELD_MAP)
        self.product_service = service or product_services.ProductService()
        self.category_service = category_service or category_services.CategoryService()

    def parse_entity(self, data: dict) -> bool:
        mapped_data = self.mapper.map_fields(data=data)
        defaults = {"ext_id": mapped_data["ext_id"]}
        instance, _ = self.product_service.create_or_update(
            defaults=defaults, **mapped_data
        )
        self._set_category(instance)

    def _set_category(self, instance) -> None:
        if instance.ext_cat_id:
            category = self.category_service.get_by_lookup(
                "ext_id", instance.ext_cat_id
            )
            if category:
                instance.category = category
                self.product_service.save(instance)
