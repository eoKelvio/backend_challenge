import threading

from fastapi import FastAPI
from src import route
from src.utils import start_consuming


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
