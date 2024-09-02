from pydantic_settings import BaseSettings
from fastapi import FastAPI
import uvicorn

app = FastAPI()

class Settings(BaseSettings):
    private_key_path: str

    class Config:
        env_file = ".env"
        extra = "ignore"  

settings = Settings()

PRIVATE_KEY_PATH = settings.private_key_path



