# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from storage.app.src.database import get_db, save_to_db
# from storage.app.models.person import Person
# from storage.app.models.account import Account
# from storage.app.models.card import Card

# router = APIRouter(prefix="/storage")

# @router.post("/person")
# def create_person(data: dict, db: Session = Depends(get_db)):
#     try:
#         return save_to_db(db, Person, data)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Erro ao salvar dados da pessoa: {e}")

# @router.post("/account")
# def create_account(data: dict, db: Session = Depends(get_db)):
#     try:
#         return save_to_db(db, Account, data)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Erro ao salvar dados da conta: {e}")

# @router.post("/card")
# def create_card(data: dict, db: Session = Depends(get_db)):
#     try:
#         return save_to_db(db, Card, data)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Erro ao salvar dados do cartão: {e}")