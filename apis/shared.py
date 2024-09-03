import pika
import json

class RabbitMQ:
    def __init__(self, url: str):
        self.connection = pika.BlockingConnection(pika.URLParameters(url))
        self.channel = self.connection.channel()

    def declare_exchange(self, exchange_name: str, exchange_type='topic'):
        self.channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)

    def publish_message(self, exchange_name: str, routing_key: str, message: dict):
        self.channel.basic_publish(
            exchange=exchange_name,
            routing_key=routing_key,
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            )
        )

    def close_connection(self):
        self.connection.close()
