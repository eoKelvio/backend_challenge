from src import route
from config import app

@app.get("/")
def root():
    return{"message":"ok"}

app.include_router(route.router)