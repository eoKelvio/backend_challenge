from sqlalchemy import Integer, String, Date, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Person:
    __tablename__ = "persons"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] 
    email: Mapped[str]
    gender: Mapped[str]
    birth_date: Mapped[Date]
    address: Mapped[str]
    salary: Mapped[float]
    cpf: Mapped[str] 

    account: Mapped["Account"] = relationship("Account", back_populates="owner") # type: ignore
