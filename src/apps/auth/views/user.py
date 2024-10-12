from src.apps.auth.use_cases import phone_registration_use_case as phone_registration
from src.apps.auth.use_cases import email_registration_use_case as email_registration
from src.apps.auth.use_cases import oauth_registration_use_case as oauth_registration
from src.base.views import use_case_generics
from ..serializers import user as user_serializers
from ..use_cases import user_auth_use_case
from ..params import params
from rest_framework.response import Response
from rest_framework import status


class UserLoginAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.UserLoginSerializer
    create_params_class = params.UserLoginParams
    create_use_case_class = user_auth_use_case.UserLoginUseCase
    list_serializer_class = user_serializers.UserLoginResponseSerializer


class UserRegisterAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.UserRegisterSerializer
    create_params_class = params.UserRegister
    create_use_case_class = user_auth_use_case.UserRegisterUseCase
    list_serializer_class = user_serializers.UserListSerializer


class UserPhoneStep1RegisterAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.RegistrationPhoneNumberSerializer
    create_params_class = params.RegistrationPhoneNumberParams
    create_use_case_class = phone_registration.RegistrationPhoneNumberUseCase
    list_serializer_class = user_serializers.RegistrationPhoneNumberSerializer

    def create(self, request, *args, **kwargs):
        instance = self.perform_create(request=request, **request.data)
        return Response(
            {"data": "OTP успешно отправлен на номер телефона"},
            status=status.HTTP_200_OK,
        )


class UserPhoneStep2RegisterAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.RegistrationStep2PhoneNumberSerializer
    create_params_class = params.RegistrationStep2PhoneNumberParams
    create_use_case_class = phone_registration.RegistrationStep2PhoneNumberUseCase
    list_serializer_class = user_serializers.RegistrationPhoneNumberSerializer

    def create(self, request, *args, **kwargs):
        instance = self.perform_create(request=request, **request.data)
        return Response(status=status.HTTP_200_OK)


class UserPhoneStep3RegisterAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.UserRegisterSerializer
    create_params_class = params.UserRegister
    create_use_case_class = phone_registration.UserRegisterUseCase
    list_serializer_class = user_serializers.UserLoginResponseSerializer


class UserEmailStep1RegisterAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.RegistrationEmailSerializer
    create_params_class = params.RegistrationEmailParams
    create_use_case_class = email_registration.RegistrationEmailUseCase
    list_serializer_class = user_serializers.RegistrationEmailSerializer

    def create(self, request, *args, **kwargs):
        instance = self.perform_create(request=request, **request.data)
        return Response(
            {"data": "OTP успешно отправлен на email"}, status=status.HTTP_200_OK
        )


class UserEmailStep2RegisterAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.RegistrationStep2EmailSerializer
    create_params_class = params.RegistrationStep2EmailParams
    create_use_case_class = email_registration.RegistrationStep2EmailUseCase
    list_serializer_class = user_serializers.RegistrationEmailSerializer

    def create(self, request, *args, **kwargs):
        instance = self.perform_create(request=request, **request.data)
        return Response(status=status.HTTP_200_OK)


class UserEmailStep3RegisterAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.UserRegisterSerializer
    create_params_class = params.UserRegister
    create_use_case_class = email_registration.UserEmailRegisterUseCase
    list_serializer_class = user_serializers.UserLoginResponseSerializer


class UserOAuthRegisterAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.RegistrationOAuthSeralizier
    create_params_class = params.RegistrationOAuthParams
    create_use_case_class = oauth_registration.RegistrationOAuthUseCase
    list_serializer_class = user_serializers.UserLoginResponseSerializer

    def create(self, request, *args, **kwargs):
        instance = self.perform_create(request=request, **request.data)
        return Response(data={"data": "Success"}, status=status.HTTP_200_OK)


class UserOAuthLoginAPIView(use_case_generics.UseCaseCreateAPIView):
    create_serializer_class = user_serializers.LoginOAuthSeralizier
    create_params_class = params.LoginOAuthParams
    create_use_case_class = oauth_registration.LoginOAuthUseCase
    list_serializer_class = user_serializers.UserLoginResponseSerializer
