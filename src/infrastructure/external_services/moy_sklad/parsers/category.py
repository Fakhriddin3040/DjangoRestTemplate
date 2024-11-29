from typing import Dict
from src.base.abstractions.services import base_service
from src.infrastructure.external_services.moy_sklad.parsers.base import MKParserBase
from src.apps.category.services import category as category_services
from ..mappers.base import MKBaseMapper
from ..mappers.category import MKCategoryMapper
from .. import const


class MKCategoryParser(MKParserBase):
    def __init__(
        self,
        mapper: MKBaseMapper = None,
        model_service: base_service.AbstractService = None,
    ) -> None:
        self.mapper = mapper or MKCategoryMapper(const.CATEGORY_FIELD_MAP)
        self.model_service = model_service or category_services.CategoryService()

    def map_and_parse_entity(self, data: Dict[str, str]) -> bool:
        mapped_data = self.map_data(data=data)
        defaults = {"ext_id": mapped_data["ext_id"]}
        instance, created = self.model_service.create_or_update(
            defaults=defaults, **mapped_data
        )

        if instance.ext_id:
            self._set_parent(instance)
        return instance, created

    def _set_parent(self, instance) -> None:
        parent = self.model_service.get_by_lookup(
            "ext_parent_title", instance.ext_parent_title
        )
        if parent:
            instance.parent = parent
            self.model_service.save(instance)
