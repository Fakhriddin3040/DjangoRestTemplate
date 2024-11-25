from . import base as base_apis
from .. import const as moy_sklad_const


class MKCategoryAPI(base_apis.MKModelAPIBase):
    ENTITY_PATH = moy_sklad_const.CATEGORY_PATH
