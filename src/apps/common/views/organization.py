from src.base.views import generics
from ..repositories.organization import OrganizationRepository
from ..serializers.organization import OrganizationListSerializer


class OrganizationListAPIView(generics.ListAPIView):
    _repository = OrganizationRepository()
    list_serializer_class = OrganizationListSerializer
