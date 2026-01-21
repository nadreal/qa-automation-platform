from typing import List
from backend.app.models import User

class UserService:
    def create_user(self, user: User) -> User:
        raise NotImplementedError

    def get_user(self, user_id: int) -> User:
        raise NotImplementedError

    def list_users(self) -> List[User]:
        raise NotImplementedError

    def delete_user(self, user_id: int) -> None:
        raise NotImplementedError
