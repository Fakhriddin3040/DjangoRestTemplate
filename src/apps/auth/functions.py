import datetime
import jwt
from django.db import models as dj_models
from rest_framework_simplejwt.tokens import RefreshToken
from src.apps.auth.models import user as user_models
from rest_framework_simplejwt.tokens import Token
import hashlib
import random
import requests
import pytz
from .services import user as user_services
from src.config.settings.base import TIME_ZONE
from src.utils.functions.functions import get_datetime, send_mail
from src.apps.auth import const

tz = pytz.timezone(TIME_ZONE)


def token_for_user(user: user_models.User) -> Token:
    return RefreshToken.for_user(user)


def get_otp_expire_time():
    return datetime.datetime.now() + datetime.timedelta(minutes=5)


def send_sms_notification(phone_numbers: list | str, message: str) -> bool:
    LOGIN = "ITRUN"
    PASSWORD = "!tRunK!d$"
    MESSAGE = message

    if isinstance(phone_numbers, str):
        phone_numbers = [phone_numbers]
    phone_numbers = [str(phone).replace("+", "") for phone in phone_numbers]
    RECIPIENTS = ",".join(phone_numbers)
    APIKEY = hashlib.md5(f"{LOGIN}{PASSWORD}{MESSAGE}".encode("utf-8")).hexdigest()

    response = requests.get(
        "http://109.74.70.2:7678/sms_notification/sms.php",
        {
            "login": LOGIN,
            "apikey": APIKEY,
            "message": MESSAGE,
            "recipients": RECIPIENTS,
        },
        timeout=5,
    )

    result = int(response.text.split("<result>")[1].split("</result>")[0])
    return not bool(result)


def generate_otp(min: int = 10000, max: int = 99999) -> int:
    return random.randint(min, max)


def email_user(self, subject, message, from_email=None, **kwargs):
    """Send an email to this user."""
    send_mail(subject, message, from_email, [self.email], **kwargs)


def send_email_notification(subject: str, message: str, recipients: list | str) -> None:
    from_email = "send.message.2333@gmail.com"
    recipient_list = [recipients] if isinstance(recipients, str) else recipients

    send_mail(subject, message, from_email, recipient_list)


def decode_jwt(token: str, *args, **kwargs) -> dict[str:str]:
    decoded_token = jwt.decode(token, *args, **kwargs)
    return decoded_token


def validate_user_email_username_uniqueness(
    user_services: user_services.UserService,
    username: str,
    email: str,
) -> bool:
    user = (
        user_services.get_queryset()
        .filter(dj_models.Q(email=email) | dj_models.Q(username=username))
        .last()
    )

    if user is not None:
        if user.email == email:
            raise Exception(const.FieldsBusyExceptionMessages.USER_EMAIL)
        if user.username == username:
            raise Exception(const.FieldsBusyExceptionMessages.USER_USERNAME)


def validate_user_phone_number_username_uniqueness(
    user_service: user_services.UserService,
    username: str,
    phone_number: str,
) -> None:
    user = (
        user_service.get_queryset()
        .filter(dj_models.Q(username=username) | dj_models.Q(phone_number=phone_number))
        .last()
    )

    if user is not None:
        if user.username == username:
            raise Exception(const.FieldsBusyExceptionMessages.USER_USERNAME)
        elif user.phone_number == phone_number:
            raise Exception(const.FieldsBusyExceptionMessages.USER_PHONE_NUMBER)


def is_valid_otp_exp_time(exp_time: datetime.datetime) -> bool:
    return exp_time < get_datetime()
