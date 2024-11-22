from typing import Any, Dict, List
from src.infrastructure.external_services.moy_sklad.parsers.base import MKParserBase


class MKSyncBase:
    def __init__(self, parser: MKParserBase = None) -> None:
        self.parser = parser or MKParserBase()

    def sync(self, data: List[Dict[str, Any]]):
        self._ensure_data_type(data)
        created_count = self.parser.parse_entities(data)
        print(f"Created {created_count} categories")
        print(f"Length of data: {len(data)}")

    def _ensure_data_type(self, data: Any) -> List[Dict[str, Any]]:
        if not isinstance(data, list) and all(isinstance(item, dict) for item in data):
            raise ValueError("Data must be a list of dictionaries")
