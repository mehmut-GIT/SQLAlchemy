"""
Database Configuration Module
Centralized database settings and engine creation
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./sqlalchemy_tutorial.db"
)

# Engine creation
engine = create_engine(
    DATABASE_URL,
    echo=False,  # Set to True for debugging SQL queries
    pool_size=10,
    max_overflow=20
)

# Session factory
SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False
)

# Base class for models
Base = declarative_base()


def get_session():
    """
    Get a database session
    Usage in with statement: with get_session() as session:
    """
    return SessionLocal()


def init_db():
    """Initialize database - create all tables"""
    Base.metadata.create_all(bind=engine)
    print("✓ Database initialized successfully!")


def drop_db():
    """Drop all tables - USE WITH CAUTION"""
    Base.metadata.drop_all(bind=engine)
    print("✓ All tables dropped!")
