from http import HTTPMethod
from django.db import models

from rest_framework.response import Response
from rest_framework import views, generics
from rest_framework.settings import api_settings
from src.base.abstractions.repositories import base_django_repository
from src.base.mixins import mixins


class ModelDetailAPIView(views.APIView):
    http_method_names = [HTTPMethod.GET.lower()]
    lookup_field = "pk"
    lookup_url_kwarg = "pk"
    _repository: base_django_repository.AbstractDjangoRepository

    def get_object(self) -> models.Model:
        assert self.lookup_url_kwarg in self.kwargs, (
            "У представления {} отсутствует параметр URL-адреса "
            "для поиска объекта с идентификатором.".format(self.__class__.__name__)
        )
        return self._repository.get_by_lookup(
            lookup=self.lookup_field, value=self.kwargs[self.lookup_url_kwarg]
        )


class PaginatedAPIViewBase(views.APIView):
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS
    _repository: base_django_repository.AbstractDjangoRepository

    @property
    def paginator(self):
        if not hasattr(self, "_paginator"):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        return self.paginator.get_paginated_response(data)


class ListAPIViewBase(PaginatedAPIViewBase):
    http_method_names = [HTTPMethod.GET.lower()]

    def get_queryset(self) -> models.QuerySet:
        return self._repository.all()

    def get(self, request, *args, **kwargs) -> Response:
        """Your action here."""


class RetrieveAPIViewBase(ModelDetailAPIView):
    http_method_names = [HTTPMethod.GET.lower()]

    def get(self, request, *args, **kwargs) -> Response:
        """Your action here."""


class CreateAPIViewBase(
    views.APIView,
):
    http_method_names = [HTTPMethod.POST.lower()]

    def post(self, request, *args, **kwargs) -> Response:
        """Your action here."""


class UpdateAPIViewBase(
    ModelDetailAPIView,
):
    http_method_names = [HTTPMethod.PUT.lower()]

    def put(self, request, *args, **kwargs) -> Response:
        """Your action here."""


class DestroyAPIViewBase(
    ModelDetailAPIView,
):
    http_method_names = [HTTPMethod.DELETE.lower()]

    def delete(self, request, *args, **kwargs) -> Response:
        """Your action here."""


#! ============================================= !#


class ListAPIView(ListAPIViewBase, mixins.ListModelMixin):
    list_serializer_class = None

    def get(self, request, *args, **kwargs) -> Response:
        return self.list(request, *args, **kwargs)


class RetrieveAPIView(RetrieveAPIViewBase, mixins.RetrieveModelMixin):
    def get(self, request, *args, **kwargs) -> Response:
        return self.retrieve(request, *args, **kwargs)


class CreateAPIView(
    CreateAPIViewBase,
    mixins.CreateModelMixin,
):
    def post(self, request, *args, **kwargs) -> Response:
        return self.create(request, *args, **kwargs)


class UpdateAPIView(UpdateAPIViewBase, mixins.UpdateModelMixin):
    def put(self, request, *args, **kwargs) -> Response:
        return self.update(request, *args, **kwargs)


class DestroyAPIView(DestroyAPIViewBase, mixins.DestroyModelMixin):
    def delete(self, request, *args, **kwargs) -> Response:
        return self.destroy(request, *args, **kwargs)


class ListCreateAPIView(ListAPIView, CreateAPIView):
    pass


class CreateRetrieveAPIView(CreateAPIView, RetrieveAPIView):
    pass


class RetrieveUpdateAPIView(RetrieveAPIView, UpdateAPIView):
    pass


class RetrieveDestroyAPIView(RetrieveAPIView, DestroyAPIView):
    pass


class RetrieveUpdateDestroyAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    pass


class CRUDAPIView(
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, generics.GenericAPIView
):
    pass
