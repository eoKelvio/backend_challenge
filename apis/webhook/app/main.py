from config import app
from src.routes import webhook

app.include_router(webhook.router)
