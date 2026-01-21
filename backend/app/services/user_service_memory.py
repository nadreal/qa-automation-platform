from typing import Dict, List
from backend.app.models import User
from backend.app.services.user_service import UserService


class InMemoryUserService(UserService):
    def __init__(self):
        self._users: Dict[int, User] = {}

    def create_user(self, user: User) -> User:
        if user.id in self._users:
            raise ValueError("User already exists")
        self._users[user.id] = user
        return user

    def get_user(self, user_id: int) -> User:
        if user_id not in self._users:
            raise KeyError("User not found")
        return self._users[user_id]

    def list_users(self) -> List[User]:
        return list(self._users.values())

    def delete_user(self, user_id: int) -> None:
        if user_id not in self._users:
            raise KeyError("User not found")
        del self._users[user_id]
