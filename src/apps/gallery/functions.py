import io, base64
from PIL import Image

from src.apps.auth.const import PROFILE_AVATAR_ROOT


def image_from_base64(base64_str: str):
    img = Image.open(io.BytesIO(base64.decodebytes(bytes(base64_str, "utf-8"))))
    path = "{}{}{}".format(PROFILE_AVATAR_ROOT, img.filename, img.format)
    img.save()
    return img.path
