from fastapi import FastAPI
from src.routes import person, card, account, webhook

app = FastAPI()

app.include_router(person.router)
app.include_router(account.router)
app.include_router(card.router)
app.include_router(webhook.router)