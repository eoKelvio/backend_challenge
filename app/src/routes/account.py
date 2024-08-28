import base64
from datetime import datetime
import json
from fastapi import APIRouter, HTTPException
from src.utils import decrypt_body
from config import PRIVATE_KEY_PATH
from src.schemas import RequestSchema, AccountBody

router = APIRouter(prefix='/account')

@router.post('/')
async def person_response(request: RequestSchema):
    try:
        time = datetime.now()
        event = request.event
        encrypted_body = base64.b64decode(request.body)
        
        decrypted_body = decrypt_body(encrypted_body, PRIVATE_KEY_PATH)
        account_data_dump = json.loads(decrypted_body)
        account_data = AccountBody(**account_data_dump)
        
        return {
            "time": time,
            "event": event,
            "account": account_data.model_dump()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
