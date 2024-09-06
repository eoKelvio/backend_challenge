import time
import pika
import json
from config import RABBITMQ_URL
from fastapi.logger import logger

class RabbitMQ:
    def __init__(self):
        for _ in range(5):
            try:
                self.connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
                self.channel = self.connection.channel()
                logger.info("Connection made successfully!")
                break
            except pika.exceptions.AMQPConnectionError:
                logger.info("Connection attempt failed. Trying again in 5 seconds...")
                time.sleep(5)
        else:
            raise Exception("Unable to connect to RabbitMQ after several attempts.")

        self.declare_exchange('events')
        self.declare_queue('person_queue')
        self.declare_queue('account_queue')
        self.declare_queue('card_queue')

        self.channel.queue_bind(exchange='events', queue='person_queue', routing_key='person')
        self.channel.queue_bind(exchange='events', queue='account_queue', routing_key='account')
        self.channel.queue_bind(exchange='events', queue='card_queue', routing_key='card')

    def declare_queue(self, queue_name):
        self.channel.queue_declare(queue=queue_name, durable=True)

    def declare_exchange(self, exchange_name):
        self.channel.exchange_declare(exchange=exchange_name, exchange_type='topic', durable=True)
        
    def publish_message(self, exchange, routing_key, message):
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2)
        )

    def setup_consuming(self, queues_callbacks):
        for queue, callback in queues_callbacks.items():
            self.channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
            logger.info(f"Consumindo mensagens da fila: {queue}")

    def close_connection(self):
        self.connection.close()