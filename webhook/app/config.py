from pydantic_settings import BaseSettings
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# if __name__ == "__config__":
#     uvicorn.run("config:app", host="0.0.0.0", port=9999, reload=True)

class Settings(BaseSettings):
    private_key_path: str

    class Config:
        env_file = ".env"
        extra = "ignore"  

settings = Settings()

PRIVATE_KEY_PATH = settings.private_key_path



