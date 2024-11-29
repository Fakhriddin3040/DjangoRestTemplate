from typing import Any, Dict
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
        super().__init__(
            mapper=mapper or MKProductMapper(const.PRODUCT_FIELD_MAP),
            model_service=service or product_services.ProductService(),
        )
        self.category_service = category_service or category_services.CategoryService()

    def map_and_parse_entity(self, data: Dict[str, Any]) -> bool:
        mapped_data = self.map_data(data=data)
        defaults = self.get_defaults(mapped_data)
        instance, _ = self.model_service.create_or_update(
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
                self.model_service.save(instance)
