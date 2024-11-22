BASE_URL = "https://api.moysklad.ru/api/remap/1.2"
ENTITY_PATH = "entity"

LOOKUP_MAP = {
    "gt": ">",
    "lt": "<",
    "neq": "!=",
    "cnt": "~",
    "ncnt": "!~",
    "gte": ">=",
    "lte": "<=",
}

MK_PRODUCT_FIELD_MAP = {
    "id": "ext_id",
    "productFolder__meta__href__get_product_folder_ext_id*": "ext_cat_id",
    "name": "title",
    "description": "description",
    "salePrices__value__get_sell_price*": "price",
}

MK_CATEGORY_FIELD_MAP = {
    "id": "ext_id",
    "name": "title",
    "pathName": "ext_parent_title",
}
