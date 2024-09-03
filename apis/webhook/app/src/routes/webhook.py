import base64
from datetime import datetime
import json
from fastapi import APIRouter, HTTPException
from webhook.app.src.utils import decrypt_body
from config import PRIVATE_KEY_PATH
from webhook.app.src.schemas import RequestSchema, PersonBody, AccountBody, CardBody
from shared import RabbitMQ
import json

router = APIRouter(prefix='/webhook')

rabbitmq = RabbitMQ()
rabbitmq.declare_exchange('events')

def publish_to_rabbitmq(event_type, message):
    routing_key = f'event.{event_type}'
    rabbitmq.publish_message('events', routing_key, message)

def decrypt(request):
    time = datetime.now()
    encrypted_body = base64.b64decode(request.body)
    event = request.event
        
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
    
    publish_to_rabbitmq(event, json.dumps(data_dump))
        
    return {
        "time": time,
        "event": event,
        event: data.model_dump()
    }

@router.post('/person')
async def person_response(request: RequestSchema):
    try:
        return decrypt(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/account')
async def account_response(request: RequestSchema):
    try:
        return decrypt(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/card')
async def card_response(request: RequestSchema):
    try:
        return decrypt(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))