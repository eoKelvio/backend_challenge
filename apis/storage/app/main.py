from fastapi import FastAPI
from storage.app.src import route
from storage.app.src.utils import start_consuming
import threading

def lifespan(app: FastAPI):
    thread = threading.Thread(target=start_consuming, daemon=True)
    thread.start()
    
    yield

    if thread.is_alive():
        thread.join()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "ok"}

app.include_router(route.router)