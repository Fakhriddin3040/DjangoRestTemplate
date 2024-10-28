from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class NoMetaPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(data)