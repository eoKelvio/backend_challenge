import json
from fastapi.logger import logger
from sqlalchemy.orm import Session
from shared import RabbitMQ
from src.database import get_db, save_to_db
from models.person import Person
from models.account import Account
from models.card import Card

def person_message(ch, method, properties, body):
    session = next(get_db())  
    message = json.loads(body)
    logger.info(f"Received person message")
    
    try:
        save_to_db(session, Person, message)
    except Exception as e:
        logger.error(f"Error when saving person data: {e}")
    finally:
        session.close()

def account_message(ch, method, properties, body):
    session = next(get_db())
    message = json.loads(body)
    print(f"Received account message")
    
    try:
        save_to_db(session, Account, message)
    except Exception as e:
        logger.error(f"Error when saving person data: {e}")
    finally:
        session.close()

def card_message(ch, method, properties, body):
    session = next(get_db())
    message = json.loads(body)
    print(f"Received card message")
    
    try:
        save_to_db(session, Card, message)
    except Exception as e:
        logger.error(f"Error when saving person data: {e}")
    finally:
        session.close()

def start_consuming():
    rabbitmq = RabbitMQ()

    queues_callbacks = {
        'account_queue': account_message,
        'person_queue': person_message,
        'card_queue': card_message
    }

    rabbitmq.setup_consuming(queues_callbacks)
    rabbitmq.channel.start_consuming()
