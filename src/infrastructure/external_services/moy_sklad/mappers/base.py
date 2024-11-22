from typing import Any, Dict
from src.utils.mapping.field_mapper import FieldMapper


class MKBaseMapper(FieldMapper):
    def __init__(self, map):
        super().__init__(map)

    def map_fields(self, data):
        new_data = {}
        for key in self.map.keys():
            value = self._parse_value(data=data, key=key)
            new_data[self.map[key]] = value
        return new_data

    def _parse_value(self, data: Dict[str, Any], key: str) -> str:
        parts = key.split("__")
        if len(parts) == 1:
            return data.get(key)

        elif len(parts) == 2 and parts[1].endswith("*"):
            if data.get(parts[0]) is None:
                return None
            target_key = parts[0]
            method_name = parts[1][:-1]
            try:
                return getattr(self, method_name)(data, target_key)
            except AttributeError:
                raise AttributeError(
                    f"Method {method_name} not found in {self.__class__.__name__}"
                )

        if data.get(parts[0]) is None:
            return None

        return self._parse_value(data[parts[0]], "__".join(parts[1:]))
