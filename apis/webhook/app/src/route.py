import base64
import json

from config import PRIVATE_KEY_PATH
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from shared import RabbitMQ
from src.schemas import AccountBody, CardBody, PersonBody, RequestSchema
from src.utils import decrypt_body

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
def person_response(request: RequestSchema):
    try:
        body = decrypt(request)
        rabbitmq.publish_message('events', 'person', body)
        return {
            "message": "Mensagem enviada com sucesso!"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/account')
def account_response(request: RequestSchema):
    try:
        body = decrypt(request)
        rabbitmq.publish_message('events', 'account', body)
        return {
            "message": "Mensagem enviada com sucesso!"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/card')
def card_response(request: RequestSchema):
    try:
        body = decrypt(request)
        rabbitmq.publish_message('events', 'card', body)
        return {
            "message": "Mensagem enviada com sucesso!"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
