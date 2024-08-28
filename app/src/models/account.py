import enum
from sqlalchemy.orm import relationship
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Date
from database import Base

class StatusEnum(enum.Enum):
    PENDENT = 0
    ACTIVE = 1
    SUSPENDED = 2
    CLOSED = 3

class Account(Base):
    __tablename__= "accounts"

    account_id = Column(Integer, primary_key=True)
    status_id = Column(Integer, enum(StatusEnum), nullable=False, default=0)
    due_day = Column(Integer, nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'), nullable=False)
    balance = Column(Float, nullable=False)
    avaliable_balance = Column(Float, nullable=False)

    owner = relationship("Person", back_populates="account")
    card = relationship("Card", back_populates="owner")