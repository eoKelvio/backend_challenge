from sqlalchemy import Integer, String, Date, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column
from storage.app.src.database import mapper_registry

@mapper_registry.mapped
class Person:
    __tablename__ = "persons"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=False)
    email: Mapped[str] = mapped_column(String(30), unique=True, index=True)
    gender: Mapped[str] = mapped_column(String(10))
    birth_date: Mapped[Date] = mapped_column(Date, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    salary: Mapped[float] = mapped_column(Float, nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)

    account: Mapped["Account"] = relationship("Account", back_populates="owner") # type: ignore
