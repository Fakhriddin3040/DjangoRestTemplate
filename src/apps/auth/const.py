import enum
from rest_framework.settings import settings


class FieldsBusyExceptionMessages(enum.Enum):
    USER_USERNAME: str = "Данное имя пользователя занято"
    USER_PHONE_NUMBER: str = "Данный номер телефона занят"
    USER_EMAIL: str = "Данный email занят"


PROFILE_AVATAR_URL = "avatar/"
PROFILE_AVATAR_ROOT = "{}/{}".format(settings.MEDIA_ROOT, PROFILE_AVATAR_URL)
