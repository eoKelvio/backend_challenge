from pydantic_settings import BaseSettings
from fastapi import FastAPI
import uvicorn

class Settings(BaseSettings):
    private_key_path: str
    database_url: str

    class Config:
        env_file = ".env"
        extra = "ignore"  

settings = Settings()

PRIVATE_KEY_PATH = settings.private_key_path
DATABASE_URL = settings.database_url

app = FastAPI()

# if __name__ == "__config__":
#     uvicorn.run("config:app", host="0.0.0.0", port=9999, reload=True)
