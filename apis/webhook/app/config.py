from fastapi import FastAPI

from shared import RabbitMQ

app = FastAPI()
rabbitmq = RabbitMQ()
