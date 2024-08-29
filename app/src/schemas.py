from pydantic import BaseModel
from datetime import date

class RequestSchema(BaseModel):
    body: str

class PersonBody(BaseModel):
    id: int
    name: str
    email: str
    gender: str
    birth_date: date
    address: str
    salary: float
    cpf: str

class AccountBody(BaseModel):
    id: int
    status_id: int
    due_day: int
    person_id: int
    balance: float
    avaliable_balance: float

class CardBody(BaseModel):
    id: int
    card_number: str
    account_id: int
    status_id: int
    limit: float
    expiration_date: str