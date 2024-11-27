from rest_framework.response import Response

from src.base.mixins import mixins
from src.base.views import local_generics


class UseCaseCreateAPIView(
    local_generics.CreateAPIViewBase,
    mixins.UseCaseCreateModelMixin,
):
    def post(self, request, *args, **kwargs) -> Response:
        return self.create(request, *args, **kwargs)


class UseCaseUpdateAPIView(
    local_generics.UpdateAPIViewBase,
    mixins.UseCaseUpdateModelMixin,
):
    def put(self, request, *args, **kwargs) -> Response:
        return self.update(request, *args, **kwargs)


class GenericGenericUseCaseAPIView(
    local_generics.ListAPIViewBase,
    UseCaseCreateAPIView,
    UseCaseUpdateAPIView,
):
    pass


#! ================================ #!
