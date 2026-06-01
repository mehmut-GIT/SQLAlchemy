# SQLAlchemy

A comprehensive guide to getting started with **SQLAlchemy**, the popular Python SQL toolkit and Object-Relational Mapping (ORM) library.

## Project Structure

```
SQLAlchemy/
├── config.py                    # Database configuration and engine setup
├── main.py                      # Main entry point
├── models/
│   ├── __init__.py
│   └── user.py                  # User model definition
├── database/
│   ├── __init__.py
│   └── crud_operations.py       # CRUD operations for User model
├── utils/
│   ├── __init__.py
│   └── helpers.py               # Helper functions (hashing, demo data)
├── examples/
│   ├── __init__.py
│   └── crud_examples.py         # Practical CRUD examples
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Features

✨ **What's Included:**
- **User Model**: Structured SQLAlchemy ORM model with proper columns and indexes
- **CRUD Operations**: Complete Create, Read, Update, Delete operations in `UserCRUD` class
- **Database Config**: Centralized configuration for database connections
- **Helper Functions**: Utility functions for password hashing and demo data
- **Practical Examples**: Real-world usage examples with detailed comments
- **Session Management**: Proper database session handling

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Install Dependencies

```bash
pip install SQLAlchemy==2.0.29
```

Or install from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Quick Start

### 1. Run CRUD Examples

```bash
python main.py
```

This will:
- Create a SQLite database with the users table
- Create sample users
- Perform CRUD operations (Create, Read, Update, Delete)
- Display all operations with output

### 2. Use in Your Own Code

```python
from config import init_db, get_session
from database.crud_operations import UserCRUD
from utils.helpers import hash_password

# Initialize database
init_db()

# Get a session
session = get_session()
crud = UserCRUD(session)

# Create a user
user = crud.create_user(
    username='john_doe',
    email='john@example.com',
    password_hash=hash_password('password123'),
    first_name='John'
)

# Get user
user = crud.get_user_by_username('john_doe')
print(user)

# Update user
crud.update_user(user.id, email='newemail@example.com')

# Delete user
crud.delete_user(user.id)

session.close()
```

## CRUD Operations Guide

### CREATE Operations

```python
# Create single user
user = crud.create_user(
    username='user1',
    email='user1@example.com',
    password_hash=hash_password('password123'),
    first_name='John',
    last_name='Doe'
)

# Bulk create multiple users
users_data = [
    {'username': 'user1', 'email': 'user1@example.com', 'password_hash': '...'},
    {'username': 'user2', 'email': 'user2@example.com', 'password_hash': '...'},
]
users = crud.bulk_create_users(users_data)
```

### READ Operations

```python
# Get user by ID
user = crud.get_user_by_id(1)

# Get user by username
user = crud.get_user_by_username('john_doe')

# Get user by email
user = crud.get_user_by_email('john@example.com')

# Get all users (with pagination)
users = crud.get_all_users(skip=0, limit=10)

# Get active users
active_users = crud.get_active_users(skip=0, limit=10)

# Search users
results = crud.search_users('john')

# Count users
total = crud.count_users()
```

### UPDATE Operations

```python
# Update user by ID
user = crud.update_user(
    user_id=1,
    email='newemail@example.com',
    first_name='Jane'
)

# Update user by username
user = crud.update_user_by_username(
    username='john_doe',
    last_name='Smith'
)

# Deactivate user
crud.deactivate_user(user_id=1)

# Activate user
crud.activate_user(user_id=1)
```

### DELETE Operations

```python
# Delete user by ID
deleted = crud.delete_user(user_id=1)

# Delete user by username
deleted = crud.delete_user_by_username(username='john_doe')

# Soft delete (deactivate)
crud.deactivate_user(user_id=1)

# Delete all users (USE WITH CAUTION)
count = crud.delete_all_users()
```

## Database Models

### User Model

The User model includes the following columns:

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key, auto-increment |
| username | String | Unique username (indexed) |
| email | String | Unique email address (indexed) |
| password_hash | String | Hashed password |
| first_name | String | User's first name (optional) |
| last_name | String | User's last name (optional) |
| is_active | Boolean | User status (default: True) |
| created_at | DateTime | Creation timestamp |
| updated_at | DateTime | Last update timestamp |

**Indexes:**
- `username` (single column)
- `email` (single column)
- `idx_username_email` (composite)

## Configuration

### Database Connection

Edit `config.py` to change the database:

```python
# SQLite (default)
DATABASE_URL = "sqlite:///./sqlalchemy_tutorial.db"

# PostgreSQL
DATABASE_URL = "postgresql://user:password@localhost:5432/dbname"

# MySQL
DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/dbname"
```

### Disable SQL Echo

To see SQL queries during execution:

```python
engine = create_engine(
    DATABASE_URL,
    echo=True  # Set to True to see SQL statements
)
```

## Helper Functions

### Password Hashing

```python
from utils.helpers import hash_password, verify_password

# Hash a password
hashed = hash_password('mypassword')

# Verify password
is_correct = verify_password('mypassword', hashed)
```

### Demo Data

```python
from utils.helpers import generate_demo_users

demo_users = generate_demo_users()
# Returns a list of sample user dictionaries
```

## Best Practices

✅ **Do's:**
- Always close sessions: `session.close()`
- Use context managers for sessions (recommended)
- Hash passwords before storing
- Use proper error handling
- Validate input data
- Use transactions for data consistency
- Implement pagination for large result sets

❌ **Don'ts:**
- Don't hardcode database credentials
- Don't use `echo=True` in production
- Don't forget to commit/rollback transactions
- Don't store plain text passwords
- Don't skip error handling

## Examples

### Example 1: Create and Read

```python
from config import init_db, get_session
from database.crud_operations import UserCRUD
from utils.helpers import hash_password

init_db()
session = get_session()
crud = UserCRUD(session)

# Create
user = crud.create_user(
    username='alice',
    email='alice@example.com',
    password_hash=hash_password('secret'),
    first_name='Alice'
)

# Read
user = crud.get_user_by_username('alice')
print(f"User: {user.username} - {user.email}")

session.close()
```

### Example 2: Update and Delete

```python
# Update
crud.update_user(user.id, email='newemail@example.com')

# Get updated user
updated_user = crud.get_user_by_id(user.id)
print(f"New email: {updated_user.email}")

# Delete
crud.delete_user(user.id)
print("User deleted")
```

### Example 3: Search and Pagination

```python
# Search
results = crud.search_users('alice')
for user in results:
    print(user)

# Pagination
page1 = crud.get_all_users(skip=0, limit=10)
page2 = crud.get_all_users(skip=10, limit=10)
```

## Resources

- 📚 [Official SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- 🎓 [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
- 💡 [SQLAlchemy Examples](https://docs.sqlalchemy.org/en/20/faq/index.html)
- 🤝 [SQLAlchemy GitHub Repository](https://github.com/sqlalchemy/sqlalchemy)

## Common Issues and Solutions

### ModuleNotFoundError: No module named 'sqlalchemy'
```bash
pip install SQLAlchemy
```

### sqlite3.OperationalError: unable to open database file
- Ensure the directory exists
- Check write permissions
- Verify the path is correct

### IntegrityError: Duplicate key value
- Check for unique constraints (username, email)
- Ensure data is valid before inserting

## Contributing

Contributions are welcome! Feel free to:
- Report issues
- Submit pull requests
- Improve documentation
- Add new features

## License

This project is open-source and available under the MIT License.

---

**Last Updated**: June 2026

For questions or support, please refer to the [official SQLAlchemy documentation](https://docs.sqlalchemy.org/) or open an issue in this repository.
