# SQLAlchemy

A comprehensive guide to getting started with **SQLAlchemy**, the popular Python SQL toolkit and Object-Relational Mapping (ORM) library.

## Table of Contents

- [About SQLAlchemy](#about-sqlalchemy)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Database Connection](#database-connection)
- [Project Structure](#project-structure)
- [Usage Examples](#usage-examples)
- [Supported Databases](#supported-databases)
- [Resources](#resources)
- [License](#license)

## About SQLAlchemy

SQLAlchemy is a mature, feature-rich SQL toolkit and object-relational mapper (ORM) for Python. It provides a full suite of well-known enterprise-level persistence patterns designed for efficient and high-performing database access.

Whether you need a simple database connection or a complex ORM model, SQLAlchemy can handle it with flexibility and power.

## Features

✨ **Core Features:**
- **SQL Expression Language**: Write database-agnostic SQL expressions
- **Object-Relational Mapping (ORM)**: Map Python classes to database tables
- **Connection Pooling**: Efficient database connection management
- **Query API**: Intuitive and powerful query interface
- **Support for Multiple Databases**: Works with PostgreSQL, MySQL, SQLite, Oracle, and more
- **Type System**: Native Python type support for database columns
- **Transaction Management**: Built-in support for ACID transactions
- **Relationships**: Seamless one-to-one, one-to-many, and many-to-many relationships

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Install SQLAlchemy

```bash
pip install SQLAlchemy==2.0.29
```

Or install from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Install Database Driver (Optional)

Depending on your database, you may need to install an additional driver:

```bash
# PostgreSQL
pip install psycopg2-binary

# MySQL
pip install pymysql

# SQLite (built-in, no driver needed)
```

## Quick Start

### Basic Connection Example

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create engine
engine = create_engine('sqlite:///./test.db', echo=True)

# Create session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Use the session for queries
# ...
```

For a complete example, see [basic_connection.py](basic_connection.py).

## Database Connection

### Connection String Format

SQLAlchemy uses a standardized connection string format:

```
dialect+driver://username:password@host:port/database
```

### Supported Databases

#### SQLite (File-based, no server required)
```python
DATABASE_URL = "sqlite:///./test.db"
```

#### PostgreSQL
```python
DATABASE_URL = "postgresql://user:password@localhost:5432/dbname"
```

#### MySQL
```python
DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/dbname"
```

#### Oracle
```python
DATABASE_URL = "oracle://user:password@localhost:1521/dbname"
```

### Creating an Engine

```python
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///./test.db",
    echo=True,  # Print SQL statements to console
    pool_size=10,  # Connection pool size
    max_overflow=20  # Maximum overflow connections
)
```

## Project Structure

```
SQLAlchemy/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── basic_connection.py       # Basic connection example
└── [Your additional files]   # Add more examples and modules here
```

## Usage Examples

### Test Database Connection

Run the basic connection test:

```bash
python basic_connection.py
```

Expected output:
```
✓ Database connection successful!
✓ Test query result: (1,)
```

### Simple Query Example

```python
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./test.db")
Session = sessionmaker(bind=engine)
session = Session()

# Execute a query
result = session.execute(text("SELECT * FROM users"))
for row in result:
    print(row)
```

### Define Models with ORM

```python
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(engine)
```

### CRUD Operations

```python
# Create
new_user = User(username="john_doe", email="john@example.com")
session.add(new_user)
session.commit()

# Read
user = session.query(User).filter(User.username == "john_doe").first()

# Update
user.email = "newemail@example.com"
session.commit()

# Delete
session.delete(user)
session.commit()
```

## Supported Databases

SQLAlchemy supports a wide range of relational and non-relational databases:

| Database | Dialect |
|----------|---------|
| SQLite | `sqlite` |
| PostgreSQL | `postgresql` |
| MySQL | `mysql` |
| MariaDB | `mariadb` |
| Oracle | `oracle` |
| Microsoft SQL Server | `mssql` |
| Firebird | `firebird` |

## Resources

- 📚 [Official SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- 🎓 [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
- 💡 [SQLAlchemy Examples](https://docs.sqlalchemy.org/en/20/faq/index.html)
- 🤝 [SQLAlchemy GitHub Repository](https://github.com/sqlalchemy/sqlalchemy)

## Common Issues and Solutions

### Connection Issues

**Problem**: `ModuleNotFoundError: No module named 'sqlalchemy'`
- **Solution**: Install SQLAlchemy with `pip install SQLAlchemy`

**Problem**: `sqlite3.OperationalError: unable to open database file`
- **Solution**: Ensure the directory exists and you have write permissions

### Database-Specific Issues

**PostgreSQL**: Install `psycopg2-binary` for the PostgreSQL driver
```bash
pip install psycopg2-binary
```

**MySQL**: Install `pymysql` for the MySQL driver
```bash
pip install pymysql
```

## Best Practices

✅ **Do's:**
- Use connection pooling for production applications
- Close sessions explicitly or use context managers
- Define models with clear relationships
- Use transactions for data consistency
- Implement proper error handling

❌ **Don'ts:**
- Don't hardcode database credentials; use environment variables
- Don't use `echo=True` in production
- Don't forget to close database connections
- Don't skip proper exception handling

## Contributing

Contributions are welcome! Feel free to:
- Report issues
- Submit pull requests
- Improve documentation
- Add new examples

## License

This project is open-source and available under the MIT License.

---

**Last Updated**: June 2026

For questions or support, please refer to the [official SQLAlchemy documentation](https://docs.sqlalchemy.org/) or open an issue in this repository.
