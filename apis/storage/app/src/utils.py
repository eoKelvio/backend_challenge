import json

from fastapi.logger import logger
from models.account import Account
from models.card import Card
from models.person import Person
from shared import RabbitMQ
from src.database import get_db, save_to_db


def person_message(ch, method, properties, body):
    session = next(get_db())
    message = json.loads(body)
    logger.info("Received person message")
    try:
        save_to_db(session, Person, message)

        rabbitmq = RabbitMQ()
        confirmation_message = {"message": "Pessoa salva com sucesso"}
        rabbitmq.send_confirmation('person_confirmation', confirmation_message)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        logger.error(f"Error when saving person data: {e}")
    finally:
        session.close()


def account_message(ch, method, properties, body):
    session = next(get_db())
    message = json.loads(body)
    logger.info("Received account message")
    try:
        save_to_db(session, Account, message)

        rabbitmq = RabbitMQ()
        confirmation_message = {"message": "Conta salva com sucesso"}
        rabbitmq.send_confirmation('account_confirmation', confirmation_message)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        logger.error(f"Error when saving person data: {e}")
    finally:
        session.close()


def card_message(ch, method, properties, body):
    session = next(get_db())
    message = json.loads(body)
    logger.info("Received card message")
    try:
        save_to_db(session, Card, message)

        rabbitmq = RabbitMQ()
        confirmation_message = {"message": "Cartão salvo com sucesso"}
        rabbitmq.send_confirmation('card_confirmation', confirmation_message)
        ch.basic_ack(delivery_tag=method.delivery_tag)
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
