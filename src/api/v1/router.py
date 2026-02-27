from fastapi import APIRouter
from src.api.v1.endpoints.health import health_router

v1_router = APIRouter()
v1_router.include_router(health_router)