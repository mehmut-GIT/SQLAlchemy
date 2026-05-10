"""
Basic SQLAlchemy Connection Example
This script demonstrates how to create a basic database connection using SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database connection string
# Format: dialect+driver://username:password@host:port/database
# For SQLite (file-based, no external server needed):
DATABASE_URL = "sqlite:///./test.db"

# For PostgreSQL:
# DATABASE_URL = "postgresql://user:password@localhost:5432/dbname"

# For MySQL:
# DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/dbname"

# Create the SQLAlchemy engine
# echo=True prints SQL statements to console for debugging
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Set to False in production
    connect_args={"check_same_thread": False}  # SQLite specific
)

# Create a session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    """
    Dependency function to get a database session.
    Yields a session and ensures it's closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_connection():
    """Test the database connection"""
    try:
        # Get a connection from the engine
        with engine.connect() as connection:
            print("✓ Database connection successful!")
            # Execute a simple query
            result = connection.execute("SELECT 1")
            print(f"✓ Test query result: {result.fetchone()}")
    except Exception as e:
        print(f"✗ Connection failed: {e}")

if __name__ == "__main__":
    test_connection()
