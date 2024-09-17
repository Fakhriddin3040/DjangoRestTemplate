from typing import Union
from src.base.abstractions.repositories import base_django_repository as django_repo
from src.apps.auth import models as auth_models


class UserRepository(django_repo.AbstractDjangoRepository[auth_models.User]):
    model = auth_models.User

    def get_by_email(self, email: str) -> Union[auth_models.User, None]:
        return self.model.objects.filter(email=email).first()
