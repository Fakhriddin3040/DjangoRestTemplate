from rest_framework import status, settings
import io
import base64
from PIL import Image
import requests


def image_from_base64(base64_str: str):
    img = Image.open(io.BytesIO(base64.decodebytes(bytes(base64_str, "utf-8"))))
    img.save()
    return img.path

def save_image(image_bytes: bytes, filename: str) -> str:
    if not isinstance(image_bytes, bytes):
        raise TypeError("image_bytes must be type of bytes")

    f_path = settings.MEDIA_ROOT / filename

    f_path.parent.mkdir(parents=True, exist_ok=True)

    with open(f_path, "wb") as f:
        f.write(image_bytes)
    return f_path
