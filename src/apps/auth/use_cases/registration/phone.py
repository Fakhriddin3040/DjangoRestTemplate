from src.apps.auth.models import user as user_models
from src.apps.auth.services.user import UserService
from ...params import params
from src.apps.auth.functions import (
    generate_otp,
    get_otp_expire_time,
    send_sms_notification,
)


class PhoneNumberRegistrationUseCase:
    def __init__(self, user_service: UserService = None):
        self.user_service = user_service or UserService()

    def execute(self, request, params: params.PhoneNumberRegistrationParams) -> None:
        if (
            self.user_service.get_queryset()
            .filter(phone_number=params.phone_number)
            .exists()
        ):
            raise Exception("Пользователь с таким номером уже существует")

        otp = generate_otp()

        user_models.UserTempData.objects.create(
            otp=otp,
            expired_time=get_otp_expire_time(),
            target_value=params.phone_number,
        )

        send_sms_notification(params.phone_number, f"Ваш OTP код: {otp}")
