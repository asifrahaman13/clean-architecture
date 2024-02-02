# src/core/use_cases/user_service.py

from src.core.entities.user import User
from typing import Optional
from src.core.interfaces.user_interface import UserInterface
from src.infastructure.repositories.user_repository import UserRepository

class UserService(UserInterface):
    def __call__(self) -> UserInterface:
        return self
     
    def __init__(self, user_repository:UserRepository):
        # Dummy data stored in memory
        self.users = [
            User(user_id=1, username="john_doe"),
            User(user_id=2, username="jane_doe"),
        ]

        self.user_repository = user_repository

    def get_user(self, user_id: int) -> User:
        # Dummy logic to retrieve user from the in-memory list
   
    
        return self.user_repository.get_user(user_id)

    def create_user(self, user: User) -> User:
        # Logic to create user in the repository or other data source
        pass

    def update_user(self, user_id: int, updated_user: User) -> Optional[User]:
        # Logic to update user in the repository or other data source
        pass

    def delete_user(self, user_id: int) -> bool:
        # Logic to delete user from the repository or other data source
        pass