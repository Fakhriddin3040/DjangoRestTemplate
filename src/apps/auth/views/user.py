from http import HTTPMethod
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from src.apps.auth.models.user import User
from src.apps.auth.serializers.user import UserCreateSerializer, UserListSerializer


class UserAPIView(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    create_serializer = UserCreateSerializer
    list_serializer = UserListSerializer

    def get_serializer_class(self):
        if self.request.method == HTTPMethod.GET:
            return self.list_serializer
        return self.create_serializer