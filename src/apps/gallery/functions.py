from rest_framework.settings import settings
import os
from django.core.files import File
import io
import base64
from PIL import Image


def image_from_base64(base64_str: str):
    img = Image.open(io.BytesIO(base64.decodebytes(bytes(base64_str, "utf-8"))))
    img.save()
    return img.path


def save_image(image_bytes: bytes, rel_path: str, filename: str) -> str:
    if not isinstance(image_bytes, bytes):
        raise TypeError("image_bytes must be type of bytes")

    abs_path = os.path.join(settings.MEDIA_ROOT, rel_path)

    if not os.path.exists(abs_path):
        os.makedirs(abs_path, exist_ok=True)

    f_abs_path = os.path.join(abs_path, filename)
    with open(f_abs_path, "wb") as f:
        f.write(image_bytes)

    return f_abs_path


def open_as_django_file(path: str) -> File:
    if not path.startswith("/"):
        path = os.path.join(settings.MEDIA_ROOT, path)
    return File(open(path, "rb"))


def get_to_media_rel_path(abs_path: str) -> str:
    return os.path.relpath(abs_path, settings.MEDIA_ROOT)
