from typing import Any, Dict, List, Tuple
from src.base.abstractions.services import base_service
from src.utils.mapping.field_mapper import FieldMapper


class MKParserBase:
    def __init__(
        self, mapper: FieldMapper, model_service: base_service.AbstractService
    ):
        self.mapper = mapper
        self.model_service = model_service

    def map_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return self.mapper.map_fields(data)

    def map_and_parse_entity(self, data: Dict[str, Any]) -> Tuple[Any, int]:
        mapped_data = self.map_data(data)
        defaults = self.get_defaults(mapped_data)
        return self.model_service.create_or_update(defaults=defaults, **mapped_data)

    def parse_entity(self, data: Dict[str, Any]) -> Tuple[Any, int]:
        default = self.get_defaults(data)
        return self.model_service.create_or_update(defaults=default, **data)

    def map_and_parse_entities(self, data: List[Dict[str, Any]]) -> int:
        updated_count = 0
        for entity in data:
            updated_count += self.map_and_parse_entity(entity)[1]
        return updated_count

    def get_defaults(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return {"ext_id": data["ext_id"]}
