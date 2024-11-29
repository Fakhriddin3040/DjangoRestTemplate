from src.apps.gallery.services import image as image_services
from ..parsers.base import MKParserBase
from ..mappers.image import MKImageMapper


class MKImageParser(MKParserBase):
    def __init__(self, mapper=None, service=None):
        super().__init__(
            mapper=mapper or MKImageMapper(),
            model_service=service or image_services.ImageService(),
        )
