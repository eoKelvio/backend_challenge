from fastapi import APIRouter, Request, HTTPException
from src.utils import decrypt_body
from config import PRIVATE_KEY_PATH

router = APIRouter(prefix='account')

@router.post('/')
async def account(request:Request):
    try:

        data = await request.json()
        encrypted_body = data.get("body")
        
        if not encrypted_body:
            raise HTTPException(status_code=400, detail="Campo 'body' é obrigatório.")
        
        decrypted_body = decrypt_body(encrypted_body, PRIVATE_KEY_PATH)
        
        return {decrypted_body}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
