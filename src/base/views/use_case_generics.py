from rest_framework.response import Response

from src.base.mixins import mixins
from src.base.views import generics


class UseCaseCreateAPIView(
    generics.CreateAPIViewBase,
    mixins.UseCaseCreateModelMixin,
):
    def post(self, request, *args, **kwargs) -> Response:
        return self.create(request, *args, **kwargs)


class UseCaseUpdateAPIView(
    generics.UpdateAPIViewBase,
    mixins.UseCaseUpdateModelMixin,
):
    def put(self, request, *args, **kwargs) -> Response:
        return self.update(request, *args, **kwargs)


class GenericGenericUseCaseAPIView(
    generics.ListAPIViewBase,
    UseCaseCreateAPIView,
    UseCaseUpdateAPIView,
):
    pass


#! ================================ #!
