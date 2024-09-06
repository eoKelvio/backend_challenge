import json
from sqlalchemy.orm import Session
from shared import RabbitMQ
from storage.app.src.database import get_db, save_to_db
from storage.app.models.person import Person
from storage.app.models.account import Account
from storage.app.models.card import Card

def person_message(ch, method, properties, body):
    session = next(get_db())  
    message = json.loads(body)
    print(f"Mensagem de pessoa recebida: {message}")
    
    try:
        save_to_db(session, Person, message)
    except Exception as e:
        print(f"Erro ao salvar dados da pessoa: {e}")
    finally:
        session.close()

def account_message(ch, method, properties, body):
    session = next(get_db())
    message = json.loads(body)
    print(f"Mensagem de conta recebida: {message}")
    
    try:
        save_to_db(session, Account, message)
    except Exception as e:
        print(f"Erro ao salvar dados da conta: {e}")
    finally:
        session.close()

def card_message(ch, method, properties, body):
    session = next(get_db())
    message = json.loads(body)
    print(f"Mensagem de cartão recebida: {message}")
    
    try:
        save_to_db(session, Card, message)
    except Exception as e:
        print(f"Erro ao salvar dados do cartão: {e}")
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
