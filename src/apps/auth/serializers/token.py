from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    pass
