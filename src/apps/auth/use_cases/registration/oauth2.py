from rest_framework_simplejwt import tokens
from src.apps.auth.functions import decode_jwt, token_for_user
from src.apps.auth.models.user import UserTempData
from src.apps.auth.services.user import UserService
from src.base.types import BaseParams
from ...params import params as user_params
from ..user import RegistrationFinishUseCase


class OAuth2UseCase:
    def __init__(self, user_service: UserService = None):
        self.user_service = user_service or UserService()

    def execute(self, request, params: user_params.OAuth2Params) -> tokens.Token:
        user_create_params = self.get_params_from_token(token=params.token)
        user = self.user_service.get_by_email(user_create_params.email)

        if not user:
            UserTempData.objects.create(
                target_value=user_create_params.email,
                verified=True,
            )
            return RegistrationFinishUseCase().execute(
                request=request,
                params=user_create_params,
            )
        return token_for_user(user=user)

    def get_params_from_token(self, token: str) -> BaseParams:
        decoded_token = decode_jwt(
            token=token, algoritms=["RS256"], options={"verify_signature": False}
        )
        email = decoded_token.get("email")
        name = decoded_token.get("name")
        return user_params.UserRegisterParams(
            email=email,
            username=name,
            phone_number=decoded_token.get("phone_number"),
            first_name=decoded_token.get("given_name"),
            last_name=decoded_token.get("family_name"),
        )
