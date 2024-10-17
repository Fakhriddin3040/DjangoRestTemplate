from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    password = serializers.CharField()
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
    refresh = serializers.CharField()
    access = serializers.CharField()
    profile = UserListSerializer(source='user')


class PhoneNumberRegistrationSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)


class CredentialsVerificationSerializer(serializers.Serializer):
    target_value = serializers.CharField()
    otp = serializers.CharField()


class EmailRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()


class OAuth2Serializer(serializers.Serializer):
    token = serializers.CharField()
