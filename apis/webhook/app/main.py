from webhook.app.src import route
from webhook.app.config import app

@app.get("/")
def root():
    return{"message":"ok"}

app.include_router(route.router)