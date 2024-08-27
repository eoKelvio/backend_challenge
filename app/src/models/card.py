import enum
from sqlalchemy.orm import relationship
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Date
from database import Base

class StatusEnum(enum.Enum):
    PENDENT = 0
    ACTIVE = 1
    SUSPENDED = 2
    CLOSED = 3

class Card(Base):
    __tablename__="cards"

    card_id = Column(Integer, primary_key=True)
    card_number = Column(String(16), nullable=False)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    status_id = Column(Integer, enum(StatusEnum), nullable=False)
    limit = Column(Float, nullable=False)
    expiration_date = Column(String, nullable=False)

    owner = relationship("Account", back_populates="card")

class CardRequest(Base):
    time = Column(DateTime)
    body = Column(String)
    event = Column(String)