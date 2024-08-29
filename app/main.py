from fastapi import FastAPI
from src.database import Base, connection, engine
from src.routes import webhook
from src.models.person import Person
from src.models.account import Account
from src.models.card import Card

app = FastAPI()
app.include_router(webhook.router)
connection()
Base.metadata.create_all(bind=engine)


