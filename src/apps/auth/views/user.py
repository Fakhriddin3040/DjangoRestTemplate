from src.base.views import use_case_generics
from ..serializers import user as user_serializers
from ..use_cases import user_use_cases
from ..params import params


class UserLoginAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.UserLoginSerializer
    create_params_class = params.UserLoginParams
    create_use_case_class = user_use_cases.UserLoginUseCase
    list_serializer_class = user_serializers.UserLoginResponseSerializer


class UserRegisterAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.UserRegisterSerializer
    create_params_class = params.UserRegister
    create_use_case_class = user_use_cases.UserRegisterUseCase
    list_serializer_class = user_serializers.UserListSerializer
