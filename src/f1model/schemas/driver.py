from pydantic import BaseModel, ConfigDict
from datetime import datetime, date


class DriverCreate(BaseModel):
    driver_ref: str
    first_name: str
    last_name: str
    code: str | None = None
    number: int | None = None
    country: str | None = None
    date_of_birth: date | None = None
    is_active: bool = True
    jolpica_driver_id: str | None = None


class DriverRead(BaseModel):
    id: int
    driver_ref: str
    first_name: str
    last_name: str
    code: str | None
    number: int | None
    country: str | None
    date_of_birth: date | None
    is_active: bool
    jolpica_driver_id: str | None
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)


class DriverUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    code: str | None = None
    number: int | None = None
    country: str | None = None
    date_of_birth: date | None = None
    is_active: bool | None = None
