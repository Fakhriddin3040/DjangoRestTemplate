from ..models.social_media import SocialMedia

from src.base.abstractions.repositories.base_django_repository import (
    AbstractDjangoRepository,
)


class SocialMediaRepository(AbstractDjangoRepository[SocialMedia]):
    model = SocialMedia