from ..models.organization import Organization

from src.base.abstractions.repositories.base_django_repository import (
    AbstractDjangoRepository,
)


class OrganizationRepository(AbstractDjangoRepository[Organization]):
    model = Organization
