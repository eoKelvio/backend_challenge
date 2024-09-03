import json
from sqlalchemy.orm import Session
from storage.app.src.database import get_db
from storage.app.models.account import Account
from storage.app.models.card import Card
from storage.app.models.person import Person
from shared import RabbitMQ

def save_to_db(db: Session, model, data):
    try:
        db_obj = model(**data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    except Exception as e:
        db.rollback()
        raise Exception(f"Error saving to database: {str(e)}")

def process_message(ch, method, properties, body, db: Session):
    try:
        message = json.loads(body)
        event = method.routing_key.split('.')[1]

        if event == "person":
            model = Person
        elif event == "account":
            model = Account
        elif event == "card":
            model = Card
        else:
            raise ValueError(f"Unknown event type: {event}")

        save_to_db(db, model, message)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Failed to process message: {e}")

def start_consuming():
    rabbitmq = RabbitMQ()
    db = next(get_db())
    rabbitmq.consume_messages("event_queue", lambda ch, method, properties, body: process_message(ch, method, properties, body, db))