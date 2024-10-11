from rest_framework_simplejwt.tokens import Token
from src.apps.auth.models import user as user_models
from src.apps.auth.services.user_service import UserService
from rest_framework_simplejwt.tokens import RefreshToken
from ..params import params
from django.utils import timezone
from django.core.exceptions import ValidationError
from src.apps.auth.functions import generate_otp, get_otp_expire_time, send_sms_notification


class UserRegisterUseCase:
    def __init__(self, user_service: UserService = None):
        self.user_service = user_service or UserService()

    def execute(self, request, params: params.UserRegister) -> user_models.User:
        params.phone_number = request.session.get('phone_number')
        print(f"User creation params: {params}")
        user = self.user_service.create(params)
        return self._token_for_user(user)

    def _token_for_user(self, user: user_models.User) -> Token:
        return RefreshToken.for_user(user)

class RegistrationPhoneNumberUseCase:
    def __init__(self, user_service: UserService = None):
        self.user_service = user_service or UserService()
    
    def execute(self, request, params: params.RegistrationPhoneNumberParams):
        if user_models.User.objects.filter(phone_number=params.phone_number).exists():
            raise ValueError("Пользователь с таким номером уже существует")
        
        otp = generate_otp()
        request.session['phone_number'] = params.phone_number

        user_temp_data = user_models.UserTempData.objects.create(
            user=None,
            otp=otp,
            expired_time=get_otp_expire_time(),
            target_value=params.phone_number
        )

        send_sms_notification(params.phone_number, f"Ваш OTP код: {otp}")



class RegistrationStep2PhoneNumberUseCase:
    def __init__(self, user_service: UserService = None):
        self.user_service = user_service or UserService()
    
    def execute(self, request, params: params.RegistrationPhoneNumberParams) -> user_models.User:
        try:
            user_temp_data = user_models.UserTempData.objects.get(
                otp=params.otp,
                target_value=request.session.get('phone_number')
            )
        except user_models.UserTempData.DoesNotExist:
            raise ValidationError("Неверный OTP")

        if user_temp_data.expired_time < timezone.now():
            raise ValidationError("Срок действия OTP истек.")
        
        user_temp_data.delete()