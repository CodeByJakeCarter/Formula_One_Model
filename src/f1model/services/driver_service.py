from sqlalchemy.orm import Session
from f1model.repositories.driver_repository import DriverRepository

class DriverService:
    def __init__(self, session: Session):
        self.session = session
        self.repo = DriverRepository(self.session)