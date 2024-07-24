from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ..serializers.token import (
    CustomTokenObtainPairSerializer,
    CustomTokenRefreshSerializer,
)


class CustomTokenObtainPairView(TokenObtainPairView):
    _serializer_class = None
    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenRefreshView(TokenRefreshView):
    _serializer_class = None
    serializer_class = CustomTokenRefreshSerializer
