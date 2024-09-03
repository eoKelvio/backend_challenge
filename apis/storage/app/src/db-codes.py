import base64
from datetime import datetime
import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.account import Account
from src.models.card import Card
from src.models.person import Person
from src.utils import decrypt_body
from config import PRIVATE_KEY_PATH
from src.schemas import RequestSchema, PersonBody, AccountBody, CardBody

router = APIRouter(prefix='/webhook')

def save_to_db(db: Session, model, data):
    try:
        db_obj = model(**data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error saving to database: {str(e)}")

def decrypt(request, event, db: Session):
    time = datetime.now()
    encrypted_body = base64.b64decode(request.body)
        
    decrypted_body = decrypt_body(encrypted_body, PRIVATE_KEY_PATH)
    data_dump = json.loads(decrypted_body)
    
    if event == "person":
        data = PersonBody(**data_dump)
        model = Person
    elif event == "account":
        data = AccountBody(**data_dump)
        model = Account
    elif event == "card":
        data = CardBody(**data_dump)
        model = Card
    else:
        raise ValueError(f"Unknown event type: {event}")
    
    saved_data = save_to_db(db, model, data.model_dump())
    
    return {
        "time": time,
        "event": event,
        event: saved_data
    }

@router.post('/person')
async def person_response(request: RequestSchema, db: Session = Depends(get_db)):
    try:
        event = "person"
        return decrypt(request, event, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/account')
async def account_response(request: RequestSchema, db: Session = Depends(get_db)):
    event = "account"
    try:
        return decrypt(request, event, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/card')
async def card_response(request: RequestSchema, db: Session = Depends(get_db)):
    event = "card"
    try:
        return decrypt(request, event, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))