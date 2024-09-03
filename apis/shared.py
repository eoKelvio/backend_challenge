import pika
import json
from config import RABBITMQ_URL

class RabbitMQ:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
        self.channel = self.connection.channel()

    def declare_exchange(self, exchange_name):
        self.channel.exchange_declare(exchange=exchange_name, exchange_type='topic', durable=True)

    def publish_message(self, exchange, routing_key, message):
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2)  # Make message persistent
        )

    def consume_messages(self, queue, callback):
        self.channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()

    def close_connection(self):
        self.connection.close()
