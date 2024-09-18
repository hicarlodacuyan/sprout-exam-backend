"""
This module contains SQLAlchemy models for the employees.
"""
import uuid
from datetime import date
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class RegularEmployee(Base):
    __tablename__ = "regular_employees"

    id: Mapped[SQLAlchemyUUID] = mapped_column(
        SQLAlchemyUUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False
    )
    first_name: Mapped[str] = mapped_column(index=True)
    last_name: Mapped[str] = mapped_column(index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    number_of_leaves: Mapped[int] = mapped_column()
    benefits: Mapped[str] = mapped_column()

class ContractualEmployee(Base):
    __tablename__ = "contractual_employees"

    id: Mapped[SQLAlchemyUUID] = mapped_column(
        SQLAlchemyUUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False
    )
    first_name: Mapped[str] = mapped_column(index=True)
    last_name: Mapped[str] = mapped_column(index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    contract_end_date: Mapped[date] = mapped_column()
    project: Mapped[str] = mapped_column()
