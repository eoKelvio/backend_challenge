from storage.app.config import app
from storage.app.src import route

@app.get("/")
def root():
    return{"message":"ok"}

app.include_router(route.router)