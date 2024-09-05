import enum
from sqlalchemy import Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column

class StatusEnum(enum.Enum):
    PENDENT = 0
    ACTIVE = 1
    SUSPENDED = 2
    CLOSED = 3

class Card:
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    card_number: Mapped[str] = mapped_column(String(16), nullable=False)
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey('accounts.id'))
    status_id: Mapped[StatusEnum] = mapped_column(Enum(StatusEnum), nullable=False, default=0, )
    limit: Mapped[float] = mapped_column(Float, nullable=False)
    expiration_date: Mapped[str] = mapped_column(String, nullable=False)

    owner: Mapped["Account"] = relationship("Account", back_populates="card") # type: ignore
