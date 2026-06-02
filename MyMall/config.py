import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Database Setup
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./mymall.db')
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_session():
    return SessionLocal()

def init_db():
    Base.metadata.create_all(bind=engine)
    print('✓ Database initialized!')

def drop_db():
    Base.metadata.drop_all(bind=engine)
    print('✓ All tables dropped!')
