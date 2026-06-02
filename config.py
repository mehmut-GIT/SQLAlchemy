# config.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1️⃣ Create an Engine (connection to database)
engine = create_engine("sqlite:///./sqlalchemy_tutorial.db")

# 2️⃣ Create a Session Factory (to manage database sessions)
SessionLocal = sessionmaker(bind=engine)

# 3️⃣ Create a Base Class (parent for all models)
Base = declarative_base()

# 4️⃣ Helper functions
def get_session():
    return SessionLocal()

def init_db():
    Base.metadata.create_all(bind=engine)










def drop_db():
    """Drop all tables - USE WITH CAUTION"""
    Base.metadata.drop_all(bind=engine)

