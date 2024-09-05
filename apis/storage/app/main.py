from storage.app.config import app
from storage.app.src import route
from storage.app.src.database import create_tables

app.include_router(route.router)
create_tables()