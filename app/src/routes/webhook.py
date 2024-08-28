import base64
from datetime import datetime
import json
from fastapi import APIRouter, HTTPException
from src.utils import decrypt_body
from config import PRIVATE_KEY_PATH
from src.schemas import RequestSchema, PersonBody, AccountBody, CardBody

router = APIRouter(prefix='/webhook')

def decrypt(request, event):
    time = datetime.now()
    encrypted_body = base64.b64decode(request.body)
        
    decrypted_body = decrypt_body(encrypted_body, PRIVATE_KEY_PATH)
    data_dump = json.loads(decrypted_body)
    
    if event == "person":
        data = PersonBody(**data_dump)
    elif event == "account":
        data = AccountBody(**data_dump)
    elif event == "card":
        data = CardBody(**data_dump)
    else:
        raise ValueError(f"Unknown event type: {event}")
        
    return {
        "time": time,
        "event": event,
        event: data.model_dump()
    }

@router.post('/person')
async def person_response(request: RequestSchema):
    try:
        event = "person"
        return decrypt(request, event)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/account')
async def account_response(request: RequestSchema):
    event = "account"
    try:
        return decrypt(request, event)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/card')
async def card_response(request: RequestSchema):
    event = "card"
    try:
        return decrypt(request, event)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))