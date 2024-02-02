# src/application/main.py

from fastapi import FastAPI
from src.application.web.controllers import user_controller

app = FastAPI()

app.include_router(user_controller.router, prefix="/users", tags=["users"])
