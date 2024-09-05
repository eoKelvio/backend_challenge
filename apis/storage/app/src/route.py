from fastapi import APIRouter, Request
from storage.app.src.database import get_db, save_to_db
from storage.app.models.account import Account
from storage.app.models.card import Card
from storage.app.models.person import Person

router = APIRouter(prefix='/storage')

@router.post('/person')
async def person_save(request: Request):
    data = await request.json()
    db = next(get_db())
    try:
        await save_to_db(db, Person, data)
        return {'status': 'success', 'message': 'Person Saved'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
    finally:
        db.close()

@router.post('/account')
async def account_save(request: Request):
    data = await request.json()
    db = next(get_db())
    try:
        await save_to_db(db, Account, data)
        return {'status': 'success', 'message': 'Account Saved'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
    finally:
        db.close()

@router.post('/card')
async def card_save(request: Request):
    data = await request.json()
    db = next(get_db())
    try:
        await save_to_db(db, Card, data)
        return {'status': 'success', 'message': 'Card Saved'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
    finally:
        db.close()
