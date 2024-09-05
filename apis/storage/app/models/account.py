from sqlalchemy import Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Account:
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    status_id: Mapped[int]
    due_day: Mapped[int]
    person_id: Mapped[int] = mapped_column(Integer, ForeignKey('persons.id'), nullable=False)
    balance: Mapped[float]
    avaliable_balance: Mapped[float]

    owner: Mapped["Person"] = relationship("Person", back_populates="account") # type: ignore
    card: Mapped["Card"] = relationship("Card", back_populates="owner") # type: ignore
