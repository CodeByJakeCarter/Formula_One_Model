from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from f1model.db.deps import get_db
from f1model.schemas.driver import DriverCreate, DriverRead
from f1model.services.driver_service import DriverService

driver_router = APIRouter(prefix="/drivers", tags=["drivers"])

@driver_router.post("/", response_model=DriverRead)
def create_driver(
    data: DriverCreate,
    session: Session = Depends(get_db)
):
    service = DriverService(session)
    driver = service.create_driver(data)
    return driver