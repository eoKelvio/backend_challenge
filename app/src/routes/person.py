import base64
from datetime import datetime
import json
from fastapi import APIRouter, HTTPException
from src.utils import decrypt_body
from config import PRIVATE_KEY_PATH
from src.schemas import RequestSchema, PersonBody

router = APIRouter(prefix='/person')

@router.post('/')
async def person_response(request: RequestSchema):
    try:
        time = datetime.now()
        event = request.event
        encrypted_body = base64.b64decode(request.body)
        
        decrypted_body = decrypt_body(encrypted_body, PRIVATE_KEY_PATH)
        person_data_dump = json.loads(decrypted_body)
        person_data = PersonBody(**person_data_dump)
        
        return {
            "time": time,
            "event": event,
            "person": person_data.model_dump()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
