from dataclasses import dataclass
import datetime
from decimal import Decimal
from typing import List


@dataclass
class ProductCreateParams:
    ext_id: str = None
    ext_cat_id: str = None
    title: str = None
    description: str = None
    price: Decimal = None
    # images: str = Nonemodels.ManyToManyField(
    #     to="gallery.Image",
    #     verbose_name="Изображения",
    #     related_name="product_images"
    # )
    category: int = None
    on_sale: bool = None
    discount: Decimal = None
    created_at: datetime.datetime = None
    updated_at: datetime.datetime = None
    count: Decimal = None
    weight: Decimal = None
    brand: str = None
    model: List[str] = None
    colors: List[str] = None
    vendor_code: str = None
    production_year: int = None


class ProductUpdateParams:
    identifier: str = None
