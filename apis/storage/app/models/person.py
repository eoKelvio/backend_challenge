from sqlalchemy import Integer, String, Date, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.database import Base

class Person(Base):
    __tablename__ = "persons"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    gender: Mapped[str] = mapped_column(String)
    birth_date: Mapped[str] = mapped_column(Date)
    address: Mapped[str] = mapped_column(String)
    salary: Mapped[float] = mapped_column(Float)
    cpf: Mapped[str] = mapped_column(String)

    account: Mapped["Account"] = relationship("Account", back_populates="owner") # type: ignore
