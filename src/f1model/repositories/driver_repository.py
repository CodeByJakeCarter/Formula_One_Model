from sqlalchemy.orm import Session
from f1model.models.driver import Driver

class DriverRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, driver_id: int) -> Driver | None:
        return self.session.query(Driver).filter(Driver.id == driver_id).first()
    
    def get_by_driver_ref(self, driver_ref: str) -> Driver | None:
        return self.session.query(Driver).filter(Driver.driver_ref == driver_ref).first()
    
    def create(self, driver: Driver) -> Driver:
        self.session.add(driver)
        return driver
    
    def list(self, limit: int = 100, offset: int = 0) -> list[Driver]:
        return self.session.query(Driver).offset(offset).limit(limit).all()
    
    def delete(self, driver: Driver) -> None:
        self.session.delete(driver)
