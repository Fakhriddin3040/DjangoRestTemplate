from src.apps.common.paginations import NoMetaPagination
from src.base.views import local_generics
from ..repositories.organization import OrganizationRepository
from ..serializers.organization import OrganizationListSerializer


class OrganizationListAPIView(local_generics.ListAPIView):
    _repository = OrganizationRepository()
    list_serializer_class = OrganizationListSerializer
    pagination_class = NoMetaPagination
