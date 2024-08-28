import os

PRIVATE_KEY_PATH = os.getenv("PRIVATE_KEY_PATH", "./private_key.pem")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:244466666@postgres:5432/dbc")