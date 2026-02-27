from f1model.db.base import Base
from sqlalchemy.orm import mapped_column, Mapped
from datetime import date, datetime
from sqlalchemy import func, text

class Driver(Base):
    __tablename__ = "drivers"

    id: Mapped[int] = mapped_column(primary_key=True)
    driver_ref: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    code: Mapped[str | None] = mapped_column(nullable=True)
    number: Mapped[int | None] = mapped_column(nullable=True)
    country: Mapped[str | None] = mapped_column(nullable=True)
    date_of_birth: Mapped[date | None] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(server_default=text("true"))
    jolpica_driver_id: Mapped[str | None] = mapped_column(unique=True, nullable=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
