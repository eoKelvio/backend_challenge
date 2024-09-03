import enum
from sqlalchemy import Integer, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from storage.app.src.database import mapper_registry

class StatusEnum(enum.Enum):
    PENDENT = 0
    ACTIVE = 1
    SUSPENDED = 2
    CLOSED = 3

@mapper_registry.mapped
class Account:
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    status_id: Mapped[StatusEnum] = mapped_column(Enum(StatusEnum), nullable=False, default=StatusEnum.PENDENT)
    due_day: Mapped[int] = mapped_column(Integer, nullable=False)
    person_id: Mapped[int] = mapped_column(Integer, ForeignKey('persons.id'), nullable=False)
    balance: Mapped[float] = mapped_column(Float, nullable=False)
    avaliable_balance: Mapped[float] = mapped_column(Float, nullable=False)

    owner: Mapped["Person"] = relationship("Person", back_populates="account") # type: ignore
    card: Mapped["Card"] = relationship("Card", back_populates="owner") # type: ignore
