from dataclasses import dataclass


@dataclass
class ProductCreateParams:
    identifier: str = None


@dataclass
class ProductUpdateParams:
    identifier: str = None
