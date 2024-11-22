from src.base.abstractions.services.base_service import AbstractService


def validate_product_field_uniquness(
    field: str, value: str, product_service: AbstractService, **kwargs
) -> None:
    if product_service.exists(**{field: value, **kwargs}):
        raise Exception(f"Product with '{field}' {value} already exists")
