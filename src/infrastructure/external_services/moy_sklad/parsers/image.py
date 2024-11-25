from typing import Any, Dict
from src.apps.gallery.services import image as image_services
from ..parsers.base import MKParserBase
from ..mappers.image import MKImageMapper


class MKImageParser(MKParserBase):
    def __init__(self, mapper, service):
        super().__init__(
            mapper=mapper or MKImageMapper(),
            service=service or image_services.ImageService(),
        )
