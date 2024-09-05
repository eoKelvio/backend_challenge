from webhook.app.src import route
from webhook.app.config import app

app.include_router(route.router)