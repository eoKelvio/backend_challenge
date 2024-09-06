from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, registry
from storage.app.config import DATABASE_URL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
mapper_registry = registry()

def save_to_db(db: Session, model, data):
    try:
        db_obj = model(**data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    except Exception as e:
        db.rollback()
        raise Exception(f"Error saving to database: {str(e)}")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()