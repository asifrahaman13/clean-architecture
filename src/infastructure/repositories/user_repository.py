# src/infrastructure/repositories/user_repository.py

from src.core.entities.user import User
from typing import Optional

class UserRepository:
    def __init__(self):
        # In-memory "database"
        self.user_data = {
            1: User(user_id=1, username="john_doe"),
            2: User(user_id=2, username="jane_doe"),
        }

    def get_user(self, user_id: int) -> Optional[User]:
        # Simulate database interaction to get user
        print("Getting user from the database")
        return self.user_data.get(user_id)

    def create_user(self, user: User) -> User:
        # Simulate database interaction to create user
        print("Creating user in the database")
        user_id = max(self.user_data.keys()) + 1
        user.user_id = user_id
        self.user_data[user_id] = user
        return user

    def update_user(self, user_id: int, updated_user: User) -> Optional[User]:
        # Simulate database interaction to update user
        print(f"Updating user with ID {user_id} in the database")
        if user_id in self.user_data:
            self.user_data[user_id] = updated_user
            return updated_user
        return None

    def delete_user(self, user_id: int) -> bool:
        # Simulate database interaction to delete user
        print(f"Deleting user with ID {user_id} from the database")
        if user_id in self.user_data:
            del self.user_data[user_id]
            return True
        return False
