from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    password = serializers.CharField()
    username = serializers.CharField(max_length=25)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)
    birth_date = serializers.DateField(required=False)


class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()


class UserUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    password = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)


class UserListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    birth_date = serializers.DateField()


class UserLoginResponseSerializer(serializers.Serializer):
    refresh = serializers.CharField(source="__str__")
    access = serializers.CharField(source="access_token")


class RegistrationPhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)


class RegistrationStep2PhoneNumberSerializer(serializers.Serializer):
    otp = serializers.CharField()


class RegistrationEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

class RegistrationStep2EmailSerializer(serializers.Serializer):
    otp = serializers.CharField()

class RegistrationOAuthSeralizier(serializers.Serializer):
    token = serializers.CharField()

class LoginOAuthSeralizier(serializers.Serializer):
    token = serializers.CharField()