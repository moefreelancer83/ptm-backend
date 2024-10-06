from fastapi import APIRouter
from app.api.endpoints import task

api_router = APIRouter()

api_router.include_router(task.router ,prefix="/tasks")

