from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from f1model.db.deps import get_db
from f1model.schemas.driver import DriverCreate, DriverRead
from f1model.services.driver_service import DriverService

driver_router = APIRouter(prefix="/drivers", tags=["drivers"])

@driver_router.post("/", response_model=DriverRead, status_code=201)
def create_driver(
    data: DriverCreate,
    session: Session = Depends(get_db)
):
    service = DriverService(session)
    driver = service.create_driver(data)
    return driver

@driver_router.get("/{driver_id}", response_model=DriverRead)
def get_driver(
    driver_id: int,
    session: Session = Depends(get_db)
):
    service = DriverService(session)
    driver = service.get_driver(driver_id)
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver

@driver_router.get("/", response_model=list[DriverRead])
def list_drivers(
    limit: int = 100,
    offset: int = 0,
    session: Session = Depends(get_db)
):
    service = DriverService(session)
    driver = service.list_drivers(limit=limit, offset=offset)
    return driver