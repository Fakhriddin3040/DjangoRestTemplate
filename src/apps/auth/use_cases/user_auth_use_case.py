from rest_framework_simplejwt.tokens import Token
from src.apps.auth.models import user as user_models
from src.apps.auth.services.user_service import UserService
from rest_framework_simplejwt.tokens import RefreshToken
from ..params import params


class UserLoginUseCase:
    def __init__(self, user_service: UserService = None):
        if user_service is None:
            user_service = UserService()
        self.user_service = user_service

    def execute(self, params: params.UserLoginParams) -> Token:
        user = self.user_service.get_by_email(email=params.email)
        if user is None or not self.user_service.check_password(params.password):
            raise Exception("Invalid credentials")
        return self._token_for_user(user)

    def _token_for_user(self, user: user_models.User) -> Token:
        return RefreshToken.for_user(user)


class UserRegisterUseCase:
    def __init__(self, user_service: UserService = None):
        self.user_service = user_service or UserService()

    def execute(self, params: params.UserRegister) -> user_models.User:
        return self.user_service.create(params=params)
