from rest_framework_simplejwt.tokens import Token
from src.apps.auth.functions import token_for_user
from src.apps.auth.models import user as user_models
from src.apps.auth.services.user_service import UserService
from ..params import params

class UserLoginUseCase:
    def __init__(self, user_service: UserService = None):
        if user_service is None:
            user_service = UserService()
        self.user_service = user_service

    def execute(self, params: params.UserLoginParams, *args, **kwargs) -> Token:
        user = self.user_service.get_by_email(email=params.email)
        if user is None or not user.check_password(params.password):
            raise Exception("Invalid credentials")
        return token_for_user(self, user)


class UserRegisterUseCase:
    def __init__(self, user_service: UserService = None):
        self.user_service = user_service or UserService()

    def execute(self, request, params: params.UserRegister) -> user_models.User:
        params.phone_number = request.session.get('phone_number')
        user = self.user_service.create(params)
        user = self.user_service.set_password(user, params.password)
        return token_for_user(self, user)
