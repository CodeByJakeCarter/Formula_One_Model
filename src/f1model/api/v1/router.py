from fastapi import APIRouter
from f1model.api.v1.endpoints.health import health_router
from f1model.api.v1.driver import driver_router

v1_router = APIRouter()
v1_router.include_router(health_router)
v1_router.include_router(driver_router)