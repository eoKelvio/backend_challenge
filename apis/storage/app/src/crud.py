# crud.py
from sqlalchemy.orm import Session
from models import Person, Account, Card
from schemas import PersonBody, AccountBody, CardBody

def create_person(db: Session, person: PersonBody):
    db_person = Person(
        id=person.id,
        name=person.name,
        email=person.email,
        gender=person.gender,
        birth_date=person.birth_date,
        address=person.address,
        salary=person.salary,
        cpf=person.cpf
    )
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def create_account(db: Session, account: AccountBody):
    db_account = Account(
        id=account.id,
        status_id=account.status_id,
        due_day=account.due_day,
        person_id=account.person_id,
        balance=account.balance,
        avaliable_balance=account.avaliable_balance
    )
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def create_card(db: Session, card: CardBody):
    db_card = Card(
        id=card.id,
        card_number=card.card_number,
        account_id=card.account_id,
        status_id=card.status_id,
        limit=card.limit,
        expiration_date=card.expiration_date
    )
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card