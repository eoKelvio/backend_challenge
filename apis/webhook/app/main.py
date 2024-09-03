from webhook.app.src.routes import webhook
from webhook.app.config import app

app.include_router(webhook.router)