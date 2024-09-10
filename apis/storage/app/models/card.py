from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.database import Base

class Card(Base):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    card_number: Mapped[str] = mapped_column(String(16), nullable=False)
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey('accounts.id'), nullable=False)
    status_id: Mapped[int] = mapped_column(Integer, nullable=False)
    limit: Mapped[float] = mapped_column(Float, nullable=False)
    expiration_date: Mapped[str] = mapped_column(String, nullable=False) 

    owner: Mapped["Account"] = relationship("Account", back_populates="card") # type: ignore
