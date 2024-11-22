from django.db import models
from typing import Tuple
from src.base.abstractions.services import base_service
from src.utils.mapping.field_mapper import FieldMapper


class MKParserBase:
    def __init__(
        self, mapper: FieldMapper = None, service: base_service.AbstractService = None
    ):
        self.mapper = mapper
        self.service = service

    def parse_entity(self, data) -> Tuple[models.Model, bool]:
        mapped_data = self.mapper.map_fields(data)
        defaults = {"ext_id": mapped_data["ext_id"]}
        return self.service.create_or_update(defaults=defaults, **mapped_data)

    def parse_entities(self, data):
        for entity in data:
            self.parse_entity(entity)
