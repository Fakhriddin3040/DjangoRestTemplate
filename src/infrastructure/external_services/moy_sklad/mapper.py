from typing import Any, Dict
from src.utils.mapping.field_mapper import FieldMapper


class MoySkladParser(FieldMapper):
    def map_fields(self, data):
        new_data = {}
        for key in self.map.keys():
            pairs = self._parse_value(data=data, key=key)
            new_data[self.map[key]] = pairs[1]
        return new_data

    def _parse_value(self, data: Dict[str, Any], key: str) -> str:
        parts = key.split("__")
        if len(parts) == 1:
            return data.get(key)

        elif len(parts) == 2 and parts[1].endswith("*"):
            if data.get(parts[0]) is None:
                raise KeyError(f"Error: {parts[0]} not found in mapping process")
            target_key = parts[0]
            method_name = parts[1][:-1]
            try:
                return target_key, getattr(self, method_name)(data, target_key)
            except AttributeError:
                raise AttributeError(
                    f"Method {method_name} not found in {self.__class__.__name__}"
                )

        return self._parse_value(data[parts[0]], "__".join(parts[1:]))

    def get_product_folder_ext_id(self, data: Dict[str, str], key: str):
        value = data.get(key)
        return value.split("/")[-1] if value is not None else None
