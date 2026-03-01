from sqlalchemy.orm import Session
from f1model.repositories.driver_repository import DriverRepository
from f1model.models.driver import Driver
from f1model.schemas.driver import DriverCreate
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

class DriverService:
    def __init__(self, session: Session):
        self.session = session
        self.repo = DriverRepository(self.session)
    
    def create_driver(self, data: DriverCreate) -> Driver:
        driver = Driver(**data.model_dump())
        self.repo.create(driver)

        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise HTTPException(status_code=409, detail="driver_ref already exists")

        return driver
    
    def get_driver(self, driver_id: int) -> Driver | None:
        return self.repo.get_by_id(driver_id)
    
    def list_drivers(self, limit: int = 100, offset: int = 0) -> list[Driver]:
        return self.repo.list(limit, offset)
    
    def delete_driver(self, driver_id: int) -> bool:
        driver = self.repo.get_by_id(driver_id)
        if driver is None:
            return False
        else:
            try:
                self.repo.delete(driver)
                self.session.commit()
                return True
            except Exception:
                self.session.rollback()
                raise