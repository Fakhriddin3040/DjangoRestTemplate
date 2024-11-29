HOST = "https://api.moysklad.ru"

API_KEY: str = "9903b4458420aa193f41d12c6c7205f8324a4f0f"

FILTERS_LOOKUP_MAP = {
    "gt": ">",
    "lt": "<",
    "neq": "!=",
    "cnt": "~",
    "ncnt": "!~",
    "gte": ">=",
    "lte": "<=",
}

ORDERS_LOOKUP_MAP = {
    "asc": "desc",
    "desc": "asc",
    "isnull": "asc",
    # changing the order of the sorting, cause
    # requests.get().json() returns the list in reverse order
}

PRODUCT_FIELD_MAP = {
    "id": "ext_id",
    "productFolder__meta__href__get_product_folder_ext_id*": "ext_cat_id",
    "name": "title",
    "description": "description",
    "salePrices__value__get_sell_price*": "price",
    "images__meta__href__get_images_endpoint*": "images_endpoint",
}

CATEGORY_FIELD_MAP = {
    "id": "ext_id",
    "name": "title",
    "pathName": "ext_parent_title",
}

IMAGE_FIELD_MAP = {
    "meta__downloadHref__get_image_id*": "ext_id",
    "meta__downloadHref": "url",
}

PRODUCT_PATH = "api/remap/1.2/entity/product"
CATEGORY_PATH = "api/remap/1.2/entity/productfolder"
IMAGES_DOWNLOAD_FPATH = "api/remap/1.2/download/"  # + image_id

PRODUCT_IMAGE_FORMAT = "png"
