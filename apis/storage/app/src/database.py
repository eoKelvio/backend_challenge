from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, registry
from config import DATABASE_URL


mapper_registry = registry()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

