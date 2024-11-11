from fastapi import APIRouter, Depends
from models.account import Account
from models.card import Card
from models.person import Person
from sqlalchemy.orm import Session
from src.database import get_db, save_to_db

router = APIRouter()


@router.post("/person")
def create_person(data: dict, db: Session = Depends(get_db)):
    try:
        save_to_db(db, Person, data)
        return {"message": "Person data saved successfully"}
    except Exception as e:
        return {"error": str(e)}


@router.post("/account")
def create_account(data: dict, db: Session = Depends(get_db)):
    try:
        save_to_db(db, Account, data)
        return {"message": "Account data saved successfully"}
    except Exception as e:
        return {"error": str(e)}


@router.post("/card")
def create_card(data: dict, db: Session = Depends(get_db)):
    try:
        save_to_db(db, Card, data)
        return {"message": "Card data saved successfully"}
    except Exception as e:
        return {"error": str(e)}
