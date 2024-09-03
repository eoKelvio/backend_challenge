import enum
from sqlalchemy import Table, Column, Integer, Float, ForeignKey, String, Enum
from sqlalchemy.orm import relationship
from src.database import mapper_registry

class StatusEnum(enum.Enum):
    PENDENT = 0
    ACTIVE = 1
    SUSPENDED = 2
    CLOSED = 3


card_table = Table(
    "cards",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("card_number", String(16), nullable=False),
    Column("account_id", Integer, ForeignKey('accounts.id')),
    Column("status_id", Enum(StatusEnum), nullable=False),
    Column("limit", Float, nullable=False),
    Column("expiration_date", String, nullable=False)
)

@mapper_registry.mapped
class Card:
    __table__ = card_table

    id: int
    card_number: str
    account_id: int
    status_id: StatusEnum
    limit: float
    expiration_date: str

    owner = relationship("Account", back_populates="card")
