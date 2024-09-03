from sqlalchemy import Table, Column, Integer, String, Date, Float
from sqlalchemy.orm import relationship
from src.database import mapper_registry

person_table = Table(
    "persons",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(30), unique=False),
    Column("email", String(30), unique=True, index=True),
    Column("gender", String(10)),
    Column("birth_date", Date, nullable=False),
    Column("address", String, nullable=False),
    Column("salary", Float, nullable=False),
    Column("cpf", String(11), nullable=False)
)

@mapper_registry.mapped
class Person:
    __table__ = person_table

    id: int
    name: str
    email: str
    gender: str
    birth_date: Date
    address: str
    salary: float
    cpf: str

    account = relationship("Account", back_populates="owner")
