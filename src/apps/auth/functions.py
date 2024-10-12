import jwt
from rest_framework_simplejwt.tokens import RefreshToken
from src.apps.auth.models import user as user_models
from rest_framework_simplejwt.tokens import Token
import hashlib
import random
import requests
from datetime import timedelta
import pytz
from src.config.settings.base import TIME_ZONE
from src.utils.functions.functions import get_datetime, send_mail

tz = pytz.timezone(TIME_ZONE)


def token_for_user(self, user: user_models.User) -> Token:
    return RefreshToken.for_user(user)


def get_otp_expire_time():
    return get_datetime() + timedelta(minutes=5)


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
