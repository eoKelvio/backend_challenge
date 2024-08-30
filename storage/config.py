from pydantic_settings import BaseSettings
from fastapi import FastAPI

class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = ".env"
        extra = "ignore"  

settings = Settings()

DATABASE_URL = settings.database_url

app = FastAPI()

# if __name__ == "__config__":
#     uvicorn.run("config:app", host="0.0.0.0", port=9999, reload=True)
