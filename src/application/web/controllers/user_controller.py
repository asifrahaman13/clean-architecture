# src/application/web/controllers/user_controller.py

from fastapi import APIRouter, Depends, HTTPException
from src.core.entities.user import User
from src.core.interfaces.user_interface import UserInterface
from src.core.use_cases.user_service import UserService
from src.infastructure.repositories.user_repository import UserRepository

router = APIRouter()
user_interface = UserInterface()
user_repository = UserRepository()
user_service = UserService(user_repository)


from fastapi import HTTPException


@router.get("/users/{user_id}")
async def get_user(user_id: int, user_interface: UserInterface = Depends(user_service)):
    try:
        user = user_interface.get_user(user_id)
        print("The result ")
        print(user)
        if user:
            return user.model_dump()  # Return dictionary representation of User
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=User)
async def create_user(user: User):
    return user_interface.create_user(user)


@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, updated_user: User):
    try:
        return user_interface.update_user(user_id, updated_user)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    try:
        user_interface.delete_user(user_id)
        return {"message": "User deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
