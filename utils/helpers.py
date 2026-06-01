"""
Helper Functions Module
Utility functions for common operations
"""

import hashlib
from typing import List


def hash_password(password: str) -> str:
    """
    Hash a password using SHA256
    Note: For production, use bcrypt or argon2
    
    Args:
        password: Plain text password
        
    Returns:
        Hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against its hash
    
    Args:
        plain_password: Plain text password to verify
        hashed_password: Hashed password to check against
        
    Returns:
        True if password matches, False otherwise
    """
    return hash_password(plain_password) == hashed_password


def generate_demo_users() -> List[dict]:
    """
    Generate demo user data for testing
    
    Returns:
        List of user dictionaries
    """
    demo_users = [
        {
            'username': 'john_doe',
            'email': 'john@example.com',
            'password_hash': hash_password('password123'),
            'first_name': 'John',
            'last_name': 'Doe'
        },
        {
            'username': 'jane_smith',
            'email': 'jane@example.com',
            'password_hash': hash_password('securepass456'),
            'first_name': 'Jane',
            'last_name': 'Smith'
        },
        {
            'username': 'bob_wilson',
            'email': 'bob@example.com',
            'password_hash': hash_password('mypassword789'),
            'first_name': 'Bob',
            'last_name': 'Wilson'
        },
        {
            'username': 'alice_johnson',
            'email': 'alice@example.com',
            'password_hash': hash_password('alice123'),
            'first_name': 'Alice',
            'last_name': 'Johnson'
        },
    ]
    return demo_users
