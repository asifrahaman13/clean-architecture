# src/core/entities/user.py

# src/core/entities/user.py

from pydantic import BaseModel

class User(BaseModel):
    user_id: int | None =None
    username: str | None = None

