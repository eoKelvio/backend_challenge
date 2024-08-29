from datetime import time
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL


# Configurações de conexão com o banco de dados
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def connection():
    while True:
        try:
            conn = psycopg2.connect(host='postgres',
                                    database='dbc',
                                    user='postgres',
                                    password='244466666',
                                    cursor_factory=RealDictCursor)
            cursor = conn.cursor()
            print("Database connection was successful")
            break
        except Exception as error:
            print("Connecting to database failed")
            print("Error: ", error)
            time.sleep(2)

