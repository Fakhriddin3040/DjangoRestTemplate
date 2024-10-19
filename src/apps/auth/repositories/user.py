from src.base.abstractions.repositories import base_django_repository as django_repo
from src.apps.auth import models as auth_models


class UserRepository(django_repo.AbstractDjangoRepository[auth_models.User]):
    model = auth_models.User


class ProfileRepository(django_repo.AbstractDjangoRepository[auth_models.Profile]):
    model = auth_models.Profile
