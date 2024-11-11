from config import app
from src import route


@app.get("/")
def root():
    return {"message": "ok"}


app.include_router(route.router)
