from fastapi import FastAPI
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    rabbitmq_url: str
    database_url: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
app = FastAPI()

DATABASE_URL = settings.database_url
RABBITMQ_URL = settings.rabbitmq_url
