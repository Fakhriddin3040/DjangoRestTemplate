from src.apps.common.models.organization import Organization
from ..repositories.organization import OrganizationRepository
from src.base.abstractions.services.base_service import AbstractService


class OrganizationService(AbstractService[Organization]):
    def __init__(self, repository: OrganizationRepository) -> None:
        super().__init__(repository=repository or OrganizationRepository())
