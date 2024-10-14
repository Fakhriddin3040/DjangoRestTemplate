from src.apps.auth import const
from src.apps.auth.functions import (
    generate_otp,
    get_otp_expire_time,
    send_email_notification,
)
from src.apps.auth.models import user as user_models
from src.apps.auth.services import user as user_services
from ...params import params
from django.utils.timezone import make_aware


class EmailRegistrationUseCase:
    def __init__(self, user_service: user_services.UserService = None):
        self.user_service = user_service or user_services.UserService()

    def execute(self, request, params: params.EmailRegistrationParams) -> None:
        if self.user_service.get_queryset().filter(email=params.email).exists():
            raise Exception(const.FieldsBusyExceptionMessages.USER_EMAIL)

        otp = generate_otp()

        user_models.UserTempData.objects.create(
            otp=otp,
            expired_time=make_aware(get_otp_expire_time()),
            target_value=params.email,
        )

        msg = f"Ваш OTP код:  {otp}"

        send_email_notification(
            "Подтверждение электронной почты",
            msg,
            params.email,
        )
