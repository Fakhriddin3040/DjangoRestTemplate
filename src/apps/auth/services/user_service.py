from src.base.abstractions.services import base_service as base_service
from src.apps.auth.repositories import user as user_repo
from src.apps.auth import models as auth_models


class UserService(base_service.AbstractService[auth_models.User]):
    def __init__(self, repository: user_repo.UserRepository = None):
        super().__init__(repository=repository or user_repo.UserRepository())

    def get_by_email(self, email: str) -> auth_models.User:
        return self._repository.get_by_email(email=email)

    def set_password(self, user: auth_models.User, password: str) -> auth_models.User:
        user.set_password(password)
        return self._repository.save(instance=user)

    def check_password(self, user: auth_models.User, password: str) -> bool:
        return user.check_password(password)
