from fastapi import FastAPI
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    rabbitmq_url: str
    private_key_path: str

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()

PRIVATE_KEY_PATH = settings.private_key_path
RABBITMQ_URL = settings.rabbitmq_url

app = FastAPI()