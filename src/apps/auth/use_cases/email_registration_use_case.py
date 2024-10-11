from rest_framework_simplejwt.tokens import Token
from src.apps.auth.functions import generate_otp, get_otp_expire_time, send_email_notification
from src.apps.auth.models import user as user_models
from src.apps.auth.services.user_service import UserService
from rest_framework_simplejwt.tokens import RefreshToken
from ..params import params
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.timezone import make_aware

class RegistrationEmailUseCase:
    def __init__(self, user_service: UserService = None):
        self.user_service = user_service or UserService()
    
    def execute(self, request, params: params.RegistrationEmailParams):
        if user_models.User.objects.filter(email=params.email).exists():
            raise ValueError("Пользователь с таким email уже существует")
        
        otp = generate_otp()
        request.session['email'] = params.email

        user_temp_data = user_models.UserTempData.objects.create(
            user=None,
            otp=otp,
            expired_time=make_aware(get_otp_expire_time()),
            target_value=params.email
        )

        msg = (
            f"Ваш OTP код:  {otp}"
        )

        send_email_notification(
            "Подтверждение электронной почты",
            msg,
            params.email,
        )


class RegistrationStep2EmailUseCase:
    def __init__(self, user_service: UserService = None):
        self.user_service = user_service or UserService()
    
    def execute(self, request, params: params.RegistrationEmailParams) -> user_models.User:
        try:
            user_temp_data = user_models.UserTempData.objects.get(
                otp=params.otp,
                target_value=request.session.get('email')
            )
        except user_models.UserTempData.DoesNotExist:
            raise ValidationError("Неверный OTP")

        if user_temp_data.expired_time < timezone.now():
            raise ValidationError("Срок действия OTP истек.")
        
        user_temp_data.delete()


class UserEmailRegisterUseCase:
    def __init__(self, user_service: UserService = None):
        self.user_service = user_service or UserService()

    def execute(self, request, params: params.UserRegister) -> user_models.User:
        params.email = request.session.get('email')
        user = self.user_service.create(params)
        self.user_service.set_password(user, params.password)
        return self._token_for_user(user)

    def _token_for_user(self, user: user_models.User) -> Token:
        return RefreshToken.for_user(user)
