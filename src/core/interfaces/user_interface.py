# src/core/interfaces/user_interface.py

from src.core.entities.user import User
from typing import Optional

class UserInterface:
    def get_user(self, user_id: int) -> User:
        pass

    def create_user(self, user: User) -> User:
        pass

    def update_user(self, user_id: int, updated_user: User) -> Optional[User]:
        pass

    def delete_user(self, user_id: int) -> bool:
        pass
