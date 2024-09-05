from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Card:
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    card_number: Mapped[str]
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey('accounts.id'))
    status_id: Mapped[int]
    limit: Mapped[float] 
    expiration_date: Mapped[str] 

    owner: Mapped["Account"] = relationship("Account", back_populates="card") # type: ignore
