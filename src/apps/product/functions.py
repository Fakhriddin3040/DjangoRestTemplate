from src.base.abstractions.services.base_service import AbstractService


def validate_product_identifier_uniquness(
    identifier: str, product_service: AbstractService
) -> None:
    if product_service.exists(identifier=identifier):
        raise Exception("Продукт с данным идентификатором уже существует")
