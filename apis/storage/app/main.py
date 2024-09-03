from storage.app.src.database import engine
from storage.app.src.consumer import start_consuming
from storage.app.config import app
from storage.app.models.account import Account
from storage.app.models.card import Card
from storage.app.models.person import Person
from storage.app.src.database import mapper_registry


mapper_registry.metadata.create_all(bind=engine)
start_consuming()