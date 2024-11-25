from .base import FieldMapper
from .. import const as moy_sklad_const


class MKImageMapper(FieldMapper):
    def init(self, map=None):
        super().__init__(map or moy_sklad_const.IMAGE_FIELD_MAP)