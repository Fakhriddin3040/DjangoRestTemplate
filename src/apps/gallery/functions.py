import io
import base64
from PIL import Image


def image_from_base64(base64_str: str):
    img = Image.open(io.BytesIO(base64.decodebytes(bytes(base64_str, "utf-8"))))
    img.save()
    return img.path
