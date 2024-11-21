from typing import Any, Dict, Optional
import requests


class BaseApiClient:
    """Only path for api, not endpoint. For example: api/v1"""

    """This base class example made, looking for https://api.moysklad.ru
    class is for src.infrastructure.external_services.moy_sklad.api.MoySkladAPIService"""
    BASE_URL: str = None

    """Native url for getting entities. For example:
    if get product url is: api/v1/entity/product/......
    Then OBJECT_URL will: api/v1/entity/"""
    OBJECTS_URL: str = None
    FILTERS_MAP: Dict[str, str]

    def __init__(self, api_key: str) -> None:
        if not self.BASE_URL:
            raise ValueError("BASE_URL must be set.")
        if not self.OBJECTS_URL:
            raise ValueError("OBJECTS_URL must be set.")
        if not self.FILTERS_MAP:
            raise ValueError("FILTERS_MAP must be set.")
        self.api_key = api_key

    def _get_headers(self) -> Dict[str, str]:
        """Method for declaring default headers for all
        requests on api service."""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def get_headers(self, headers: Optional[Dict[str, str]] = None):
        if headers is None:
            headers = {}

        default_headers = self._get_headers()
        default_headers.update(headers)
        return default_headers

    def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> requests.Response:
        """
        Make a GET request to the API.
        :param endpoint: API endpoint
        :param params: Query parameters
        :param headers: Custom headers
        :return Response object
        """
        url = f"{self.BASE_URL}/{endpoint}"
        try:
            response = requests.get(
                url=url, headers=self.get_headers(headers), params=params, **kwargs
            )
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            raise RuntimeError(f"Error during GET request to {url}: {e}")

    def fetch_objects(
        self,
        entity_url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, str]] = None,
        **filters,
    ) -> Dict[str, str]:
        """
        Fetch an object with optional filters and parameters.
        :param entity_url: Entity specific url.
        :param headers: Additional headers
        :param params: Query params
        :param filters: Filters for fetching object
        """
        if params is None:
            params = {}
        if filters:
            params["filter"] = self.parse_filters(**filters)

        url = f"{self.OBJECTS_URL}/{entity_url}"

        response = self.get(endpoint=url, params=params, headers=headers)
        try:
            return response.json()
        except ValueError:
            raise ValueError("Failed to parse JSON from response.")

    def parse_filters(self, **filters) -> str:
        """
        This method for parsing request filters from keyword
        args(**kwargs). You need to implement the logic of
        parsing filters for request to api service. For example,
        here is filters for api.moysklad.ru, where filters are
        query params, and symbols for filtering maps from FILTERS_MAP:
        For example:"""
        parsed_filters = []
        for key, value in filters.items():
            parts = key.split("__")
            if len(parts) == 1:
                parsed_filters.append(f"{key}={value}")
            elif len(parts) == 2:
                field, lookup = parts
                operator = self.FILTERS_MAP.get(lookup)
                if operator is None:
                    raise ValueError(
                        f"Unsupported lookup '{lookup}' in filter key '{key}'"
                    )
                parsed_filters.append(f"{field}{operator}{value}")
            else:
                raise ValueError(
                    "Invalid filter format. Use at most one '__' in filter keys"
                )

        return ";".join(parsed_filters)
