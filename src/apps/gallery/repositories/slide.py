from src.base.abstractions.repositories.base_django_repository import (
    AbstractDjangoRepository,
)
from ..models.slide import Slide


class SlideRepository(AbstractDjangoRepository[Slide]):
    model = Slide
