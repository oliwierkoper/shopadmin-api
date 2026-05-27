import os
from dotenv import load_dotenv 
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(
    bind = engine,
    autocommit = False,
    autoflush = False
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()