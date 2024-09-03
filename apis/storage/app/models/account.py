import enum
from sqlalchemy import Table, Column, Integer, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from src.database import mapper_registry

class StatusEnum(enum.Enum):
        PENDENT = 0
        ACTIVE = 1
        SUSPENDED = 2
        CLOSED = 3

account_table = Table(
    "accounts",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("status_id", Enum(StatusEnum), nullable=False, default=0),
    Column("due_day", Integer, nullable=False),
    Column("person_id", Integer, ForeignKey('persons.id'), nullable=False),
    Column("balance", Float, nullable=False),
    Column("avaliable_balance", Float, nullable=False)
)

@mapper_registry.mapped
class Account:
    __table__ = account_table

    id: int
    status_id: StatusEnum
    due_day: int
    person_id: int
    balance: float
    avaliable_balance: float

    owner = relationship("Person", back_populates="account")
    card = relationship("Card", back_populates="owner")

    
