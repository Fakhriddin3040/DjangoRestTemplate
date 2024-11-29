from django.db.models.base import Model as Model
from src.base.views import generics, use_case_generics
from ..serializers import user as user_serializers
from ..use_cases import user as user_use_cases
from ..params import params
from ..use_cases import registration as registration_use_cases
from rest_framework.response import Response
from rest_framework import status


class UserLoginAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.UserLoginSerializer
    create_params_class = params.UserLoginParams
    create_use_case_class = user_use_cases.UserLoginUseCase
    list_serializer_class = user_serializers.UserLoginResponseSerializer


class RegistrationFinishAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.UserRegisterSerializer
    create_params_class = params.UserRegisterParams
    create_use_case_class = user_use_cases.RegistrationFinishUseCase
    list_serializer_class = user_serializers.UserLoginResponseSerializer


class RetrieveMeAPIView(generics.RetrieveAPIView):
    retrieve_serializer_class = user_serializers.UserListSerializer

    def get_object(self):
        return self.request.user


class PhoneRegistrationAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.PhoneNumberRegistrationSerializer
    create_params_class = params.PhoneNumberRegistrationParams
    create_use_case_class = registration_use_cases.PhoneNumberRegistrationUseCase
    list_serializer_class = user_serializers.PhoneNumberRegistrationSerializer

    def post(self, request, *args, **kwargs):
        self.perform_create(request, **request.data)
        return Response(
            {"detail": "Код подтверждения отправлен на указанный номер телефона"},
            status=status.HTTP_201_CREATED,
        )


class UserEmailStep1RegisterAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.EmailRegistrationSerializer
    create_params_class = params.EmailRegistrationParams
    create_use_case_class = registration_use_cases.EmailRegistrationUseCase
    list_serializer_class = user_serializers.EmailRegistrationSerializer

    def post(self, request, *args, **kwargs):
        self.perform_create(request, **request.data)
        return Response(
            {
                "detail": "Код подтверждения отправлен на указанный адрес электронной почты"
            },
            status=status.HTTP_201_CREATED,
        )


class OAuthAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.OAuth2Serializer
    create_params_class = params.OAuth2Params
    create_use_case_class = registration_use_cases.OAuth2UseCase
    list_serializer_class = user_serializers.UserLoginResponseSerializer


class CredentialsVerificationAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.CredentialsVerificationSerializer
    create_params_class = params.CredentialsVerificationParams
    create_use_case_class = user_use_cases.CredentialsVerificationUseCase

    def post(self, request, *args, **kwargs):
        self.perform_create(request, **request.data)
        return Response(status=status.HTTP_200_OK)


class CreateProfileAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.ProfileSerializer
    create_params_class = params.ProfileParams
    create_use_case_class = user_use_cases.ProfileUseCase
    list_serializer_class = user_serializers.ProfileSerializer
