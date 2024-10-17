from django.db import models as dj_models
from rest_framework_simplejwt.tokens import Token
from src.apps.auth import const
from src.apps.auth.functions import token_for_user
from src.apps.auth.models import user as user_models
from src.apps.auth.services.user import UserService
from ..params import params
from src.apps.auth import functions as auth_functions


class UserLoginUseCase:
    def __init__(self, user_service: UserService = None):
        self.user_service = user_service or UserService()

    def execute(
        self, request, params: params.UserLoginParams, *args, **kwargs
    ) -> Token:
        self.request = request
        user = self.user_service.get_by_email(email=params.email)
        if user is None or not self.user_service.check_password(user, params.password):
            raise Exception("Invalid credentials")
        return token_for_user(user)


class RegistrationFinishUseCase:
    def __init__(self, user_service: UserService = None):
        self.user_service = user_service or UserService()

    def execute(self, request, params: params.UserRegisterParams) -> Token:
        usr_tmp_data = user_models.UserTempData.objects.filter(
            dj_models.Q(target_value=params.email)
            | dj_models.Q(target_value=params.phone_number),
            verified=True,
        )
        if not usr_tmp_data:
            raise Exception("Ошибка при регистрации")

        usr_tmp_data.delete()

        self.validate(request, params)
        user = self.user_service.create(params)
        user = self.user_service.set_password(user, params.password)
        token = token_for_user(user)
        return {"refresh": token, "access": token.__str__, "user": user}

    def validate(self, request, params) -> None:
        user = self.user_service.filter(
            email=params.email,
            phone_number=params.phone_number,
        ).last()

        if user is not None:
            if user.email == params.email:
                raise Exception(const.FieldsBusyExceptionMessages.USER_EMAIL)
            if user.phone_number == params.phone_number:
                raise Exception(const.FieldsBusyExceptionMessages.USER_PHONE_NUMBER)


class CredentialsVerificationUseCase:
    def __init__(self, user_service: UserService = None):
        self.user_service = user_service or UserService()

    def execute(
        self, request, params: params.CredentialsVerificationParams
    ) -> user_models.User:
        """Filtering user tmp data by opt and email, and
        if it exists, validate expired time.
        """
        user_temp_data = user_models.UserTempData.objects.filter(
            otp=params.otp,
            target_value=params.target_value,
            verified=False,
        ).last()

        if not user_temp_data:
            raise Exception("Введён некорректный секретный ключ")

        if auth_functions.is_valid_otp_exp_time(user_temp_data.expired_time):
            raise Exception("Срок действия секретного ключа истёк")

        user_temp_data.verified = True
        user_temp_data.save()
