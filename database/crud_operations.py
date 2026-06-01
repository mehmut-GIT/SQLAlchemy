"""
CRUD Operations Module
Implements Create, Read, Update, Delete operations for User model
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import desc, and_
from models.user import User


class UserCRUD:
    """
    CRUD operations for User model
    Provides Create, Read, Update, Delete functionality
    """
    
    def __init__(self, session: Session):
        """
        Initialize CRUD with database session
        
        Args:
            session: SQLAlchemy Session object
        """
        self.session = session
    
    # ===== CREATE =====
    
    def create_user(self, username: str, email: str, password_hash: str,
                    first_name: Optional[str] = None,
                    last_name: Optional[str] = None) -> User:
        """
        Create a new user
        
        Args:
            username: Unique username
            email: Unique email address
            password_hash: Hashed password
            first_name: Optional first name
            last_name: Optional last name
            
        Returns:
            Created User object
            
        Raises:
            Exception: If user already exists
        """
        try:
            # Check if user exists
            existing_user = self.session.query(User).filter(
                User.username == username
            ).first()
            
            if existing_user:
                raise ValueError(f"User '{username}' already exists")
            
            # Create new user
            new_user = User(
                username=username,
                email=email,
                password_hash=password_hash,
                first_name=first_name,
                last_name=last_name
            )
            
            self.session.add(new_user)
            self.session.commit()
            print(f"✓ User '{username}' created successfully!")
            return new_user
            
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Error creating user: {str(e)}")
    
    # ===== READ =====
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID"""
        return self.session.query(User).filter(User.id == user_id).first()
    
    def get_user_by_username(self, username: str) -> Optional[User]:
        """Get user by username"""
        return self.session.query(User).filter(User.username == username).first()
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        return self.session.query(User).filter(User.email == email).first()
    
    def get_all_users(self, skip: int = 0, limit: int = 10) -> List[User]:
        """
        Get all users with pagination
        
        Args:
            skip: Number of records to skip
            limit: Maximum records to return
            
        Returns:
            List of User objects
        """
        return self.session.query(User).offset(skip).limit(limit).all()
    
    def get_active_users(self, skip: int = 0, limit: int = 10) -> List[User]:
        """Get all active users"""
        return self.session.query(User).filter(
            User.is_active == True
        ).offset(skip).limit(limit).all()
    
    def search_users(self, query: str) -> List[User]:
        """
        Search users by username or email
        
        Args:
            query: Search query string
            
        Returns:
            List of matching User objects
        """
        search_term = f"%{query}%"
        return self.session.query(User).filter(
            (User.username.ilike(search_term)) |
            (User.email.ilike(search_term)) |
            (User.first_name.ilike(search_term)) |
            (User.last_name.ilike(search_term))
        ).all()
    
    def count_users(self) -> int:
        """Get total count of users"""
        return self.session.query(User).count()
    
    # ===== UPDATE =====
    
    def update_user(self, user_id: int, **kwargs) -> Optional[User]:
        """
        Update user fields
        
        Args:
            user_id: User ID to update
            **kwargs: Fields to update (email, first_name, last_name, is_active, etc.)
            
        Returns:
            Updated User object or None if not found
        """
        try:
            user = self.get_user_by_id(user_id)
            
            if not user:
                print(f"✗ User with ID {user_id} not found")
                return None
            
            # Update allowed fields
            allowed_fields = {
                'email', 'first_name', 'last_name',
                'is_active', 'password_hash'
            }
            
            for key, value in kwargs.items():
                if key in allowed_fields:
                    setattr(user, key, value)
            
            self.session.commit()
            print(f"✓ User {user_id} updated successfully!")
            return user
            
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Error updating user: {str(e)}")
    
    def update_user_by_username(self, username: str, **kwargs) -> Optional[User]:
        """Update user by username"""
        user = self.get_user_by_username(username)
        if user:
            return self.update_user(user.id, **kwargs)
        return None
    
    # ===== DELETE =====
    
    def delete_user(self, user_id: int) -> bool:
        """
        Delete user by ID
        
        Args:
            user_id: User ID to delete
            
        Returns:
            True if deleted, False if not found
        """
        try:
            user = self.get_user_by_id(user_id)
            
            if not user:
                print(f"✗ User with ID {user_id} not found")
                return False
            
            self.session.delete(user)
            self.session.commit()
            print(f"✓ User {user_id} deleted successfully!")
            return True
            
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Error deleting user: {str(e)}")
    
    def delete_user_by_username(self, username: str) -> bool:
        """Delete user by username"""
        user = self.get_user_by_username(username)
        if user:
            return self.delete_user(user.id)
        return False
    
    def deactivate_user(self, user_id: int) -> Optional[User]:
        """Soft delete - deactivate user instead of deleting"""
        return self.update_user(user_id, is_active=False)
    
    def activate_user(self, user_id: int) -> Optional[User]:
        """Activate a deactivated user"""
        return self.update_user(user_id, is_active=True)
    
    # ===== BATCH OPERATIONS =====
    
    def bulk_create_users(self, users_data: List[dict]) -> List[User]:
        """
        Create multiple users at once
        
        Args:
            users_data: List of user dictionaries
            
        Returns:
            List of created User objects
        """
        try:
            users = []
            for user_data in users_data:
                user = User(**user_data)
                users.append(user)
            
            self.session.add_all(users)
            self.session.commit()
            print(f"✓ {len(users)} users created successfully!")
            return users
            
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Error bulk creating users: {str(e)}")
    
    def delete_all_users(self) -> int:
        """Delete all users - USE WITH CAUTION"""
        try:
            count = self.session.query(User).count()
            self.session.query(User).delete()
            self.session.commit()
            print(f"✓ {count} users deleted!")
            return count
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Error deleting all users: {str(e)}")
