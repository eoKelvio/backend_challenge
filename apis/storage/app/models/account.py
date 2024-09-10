from sqlalchemy import Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    status_id: Mapped[int] = mapped_column(Integer, nullable=False)
    due_day: Mapped[int] = mapped_column(Integer, nullable=False)
    person_id: Mapped[int] = mapped_column(Integer, ForeignKey('persons.id'), nullable=False)
    balance: Mapped[float] = mapped_column(Float, nullable=False)
    avaliable_balance: Mapped[float] = mapped_column(Float, nullable=False)

    owner: Mapped["Person"] = relationship("Person", back_populates="account") # type: ignore
    card: Mapped["Card"] = relationship("Card", back_populates="owner") # type: ignore
