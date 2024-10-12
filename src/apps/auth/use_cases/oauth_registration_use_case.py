from src.apps.auth.functions import decode_jwt, token_for_user
from src.apps.auth.models import user as user_models
from src.apps.auth.services.user_service import UserService
from ..params import params
from ..params.params import UserRegister
import jwt
from django.db.models import Q
from django.db.models.query import QuerySet


class RegistrationOAuthUseCase:
    def __init__(self, user_service: UserService = None):
        self.user_service = user_service or UserService()

    def execute(
        self, request, params: params.RegistrationOAuthParams
    ) -> user_models.User:
        token = params.token

        try:
            decoded_token = decode_jwt(
                token=token, algoritms=["RS256"], options={"verify_signature": False}
            )
            email = decoded_token.get("email")
            name = decoded_token.get("name")
            user_params = UserRegister(
                email=email,
                username=name,
                phone_number=decoded_token.get("phone_number"),
                first_name=decoded_token.get("given_name"),
                last_name=decoded_token.get("family_name"),
            )
            user = self.user_service.get_by_email(email)

            if user_models.User.objects.filter(
                Q(phone_number=user_params.phone_number) | Q(email=user_params.email)
            ).exists():
                raise ValueError(
                    "Пользователь с таким телефоным номером или email уже существует"
                )

            if not user:
                user = self.user_service.create(user_params)
            else:
                raise Exception("Пользователь с таким email уже существует")

        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired.")
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token.")


class LoginOAuthUseCase:
    def __init__(self, user_service: UserService = None):
        self.user_service = user_service or UserService()

    def execute(self, request, params: params.LoginOAuthParams) -> user_models.User:
        token = params.token

        try:
            decoded_token = decode_jwt(
                token=token, algoritms=["RS256"], options={"verify_signature": False}
            )
            email = decoded_token.get("email")

            user = self.user_service.get_by_email(email)
            if isinstance(user, QuerySet):
                user = user.first()
            if user:
                return token_for_user(self, user)
            else:
                raise Exception("Failed login")

        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired.")
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token.")
