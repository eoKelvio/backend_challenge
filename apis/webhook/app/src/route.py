import base64
import json
import pytz
from datetime import datetime
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from webhook.app.src.utils import decrypt_body
from webhook.app.config import PRIVATE_KEY_PATH
from webhook.app.src.schemas import RequestSchema, PersonBody, AccountBody, CardBody
from shared import RabbitMQ

rabbitmq = RabbitMQ()

router = APIRouter(prefix='/webhook')

def decrypt(request):
    encrypted_body = base64.b64decode(request.body)
    event = request.event
        
    decrypted_body = decrypt_body(encrypted_body, PRIVATE_KEY_PATH)
    data_dump = json.loads(decrypted_body)
    
    if event == "person":
        body = PersonBody(**data_dump)
    elif event == "account":
        body = AccountBody(**data_dump)
    elif event == "card":
        body = CardBody(**data_dump)
    else:
        raise ValueError(f"Unknown event type: {event}")
        
    return jsonable_encoder(body)

@router.post('/person')
async def person_response(request: RequestSchema):
    try:
        time_zone = pytz.timezone('America/Sao_Paulo')
        time = datetime.now(time_zone)
        body = decrypt(request)
        event = request.event
        rabbitmq.publish_message('events', 'person', body)
        return {
            "time": time,
            "body": body,
            "event": event
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/account')
async def account_response(request: RequestSchema):
    try:
        time_zone = pytz.timezone('America/Sao_Paulo')
        time = datetime.now(time_zone)
        body = decrypt(request)
        event = request.event
        rabbitmq.publish_message('events', 'account', body)
        return {
            "time": time,
            "body": body,
            "event": event
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/card')
async def card_response(request: RequestSchema):
    try:
        time_zone = pytz.timezone('America/Sao_Paulo')
        time = datetime.now(time_zone)
        body = decrypt(request)
        event = request.event
        rabbitmq.publish_message('events', 'card', body)
        return {
            "time": time,
            "body": body,
            "event": event
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
