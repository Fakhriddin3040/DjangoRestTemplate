from src.base.abstractions.repositories.base_django_repository import (
    AbstractDjangoRepository,
)
from src.base.abstractions.services.base_service import AbstractService
from ..models.slide import Slide
from ..repositories.slide import SlideRepository


class SlideService(AbstractService[Slide]):
    def __init__(self, repository: AbstractDjangoRepository) -> None:
        super().__init__(repository or SlideRepository())
