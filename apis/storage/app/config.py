import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from storage.app.src.utils import process_message
from shared import RabbitMQ

@asynccontextmanager
async def lifespan(app: FastAPI):
    rabbitmq = RabbitMQ()

    task = asyncio.create_task(rabbitmq.consume_messages("event_queue", process_message))
    
    yield
    
    rabbitmq.close_connection()
    await task

app = FastAPI(lifespan=lifespan)


