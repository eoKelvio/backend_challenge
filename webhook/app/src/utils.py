from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import UnsupportedAlgorithm
import pika

def load_private_key(private_key_path, password=None):
    with open(private_key_path, "rb") as key_file:
        try:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=password.encode() if password else None,
            )
        except TypeError:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
            )
        except ValueError:
            raise ValueError("Incorrect password or the key is not encrypted.")
        except UnsupportedAlgorithm as e:
            raise ValueError(f"Unsupported key encryption algorithm: {e}")
    
    return private_key

def decrypt_body(encrypted_body, private_key_path, password=None):
    private_key = load_private_key(private_key_path, password=password)
    decrypted_body = private_key.decrypt(
        encrypted_body,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_body.decode('utf-8')




class RabbitMQ:
    def __init__(self, host='rabbitmq'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()

    def declare_exchange(self, exchange_name, exchange_type='topic'):
        self.channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)

    def publish_message(self, exchange_name, routing_key, message):
        self.channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message)

    def consume_messages(self, queue_name, callback):
        self.channel.queue_declare(queue=queue_name)
        self.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()

    def close(self):
        self.connection.close()
