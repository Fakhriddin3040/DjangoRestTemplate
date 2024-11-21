from typing import Dict


class FieldMapper:
    def __init__(self, map: Dict[str, str]) -> None:
        self.map = map

    def map_fields(self, data: Dict[str, str]) -> Dict[str, str]:
        """Maps fields from dictionary, using data param key's to get mapped field from self.map"""
        try:
            return {self.map[key]: value for key, value in data.items()}
        except KeyError as e:
            raise KeyError(f"Error: {e} not found in mapping process") from e
