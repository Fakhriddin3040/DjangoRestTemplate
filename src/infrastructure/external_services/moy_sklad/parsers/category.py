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
        category_service: base_service.AbstractService = None,
    ) -> None:
        self.mapper = mapper or MKCategoryMapper(const.MK_CATEGORY_FIELD_MAP)
        self.category_service = category_service or category_services.CategoryService()

    def parse_entity(self, data: Dict[str, str]) -> bool:
        mapped_data = self.mapper.map_fields(data=data)
        defaults = {"ext_id": mapped_data["ext_id"]}
        instance, created = self.category_service.create_or_update(
            defaults=defaults, **mapped_data
        )

        if instance.ext_parent_title:
            self._set_parent(instance)
        return created

    def _set_parent(self, instance) -> None:
        parent = self.category_service.get_by_lookup("title", instance.ext_parent_title)
        if parent:
            instance.parent = parent
            self.category_service.save(instance)
