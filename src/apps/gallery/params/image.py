from dataclasses import dataclass   


@dataclass
class ImageCreateParams:
    ext_id: str = None
    title: str = None
    image: str = None
    url: str = None