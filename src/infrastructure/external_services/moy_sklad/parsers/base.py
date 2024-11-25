from typing import Any, Dict, List, Tuple
from src.base.abstractions.services import base_service
from src.utils.mapping.field_mapper import FieldMapper


class MKParserBase:
    def __init__(
        self, mapper: FieldMapper, service: base_service.AbstractService
    ):
        self.mapper = mapper
        self.service = service

    def map_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return self.mapper.map_fields(data)

    def parse_entity(self, data: Dict[str, Any]) -> int:
        mapped_data = self.map_data(data)
        defaults = {"ext_id": mapped_data["ext_id"]}
        return self.service.create_or_update(defaults=defaults, **mapped_data)

    def parse_entities(self, data: List[Dict[str, Any]]) -> int:
        updated_count = 0
        for entity in data:
            updated_count += self.parse_entity(entity)[1]
        return updated_count
