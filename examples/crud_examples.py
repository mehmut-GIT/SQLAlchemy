"""
CRUD Examples Module
Practical examples of using the UserCRUD class
"""

from config import init_db, get_session
from database.crud_operations import UserCRUD
from utils.helpers import generate_demo_users, hash_password


def main():
    """Main example function"""
    
    print("\n" + "="*60)
    print("SQLAlchemy CRUD Operations Examples")
    print("="*60 + "\n")
    
    # Initialize database
    print("1. Initializing database...")
    init_db()
    
    # Get a session
    session = get_session()
    crud = UserCRUD(session)
    
    try:
        # ===== CREATE OPERATIONS =====
        print("\n--- CREATE OPERATIONS ---\n")
        
        # Create single user
        print("Creating single user:")
        user1 = crud.create_user(
            username='mehmut',
            email='mehmut@example.com',
            password_hash=hash_password('password123'),
            first_name='Mehmut',
            last_name='Dev'
        )
        print(f"Created: {user1}\n")
        
        # Bulk create users
        print("Creating multiple users in bulk:")
        demo_users = generate_demo_users()
        bulk_users = crud.bulk_create_users(demo_users)
        print(f"Created {len(bulk_users)} users\n")
        
        # ===== READ OPERATIONS =====
        print("\n--- READ OPERATIONS ---\n")
        
        # Get user by ID
        print("Get user by ID (1):")
        user = crud.get_user_by_id(1)
        if user:
            print(f"Found: {user}")
            print(f"Email: {user.email}")
            print(f"Created at: {user.created_at}\n")
        
        # Get user by username
        print("Get user by username ('john_doe'):")
        user = crud.get_user_by_username('john_doe')
        if user:
            print(f"Found: {user}\n")
        
        # Get user by email
        print("Get user by email ('jane@example.com'):")
        user = crud.get_user_by_email('jane@example.com')
        if user:
            print(f"Found: {user}\n")
        
        # Get all users
        print("Get all users:")
        all_users = crud.get_all_users(limit=5)
        for user in all_users:
            print(f"  - {user.username}: {user.email} (Active: {user.is_active})")
        print()
        
        # Get active users
        print("Get active users:")
        active_users = crud.get_active_users(limit=5)
        print(f"Total active users: {len(active_users)}\n")
        
        # Search users
        print("Search users by 'john':")
        results = crud.search_users('john')
        for user in results:
            print(f"  - {user.username}: {user.email}")
        print()
        
        # Count users
        print(f"Total users in database: {crud.count_users()}\n")
        
        # ===== UPDATE OPERATIONS =====
        print("\n--- UPDATE OPERATIONS ---\n")
        
        # Update user
        print("Updating user (ID: 2) email and first_name:")
        updated_user = crud.update_user(
            user_id=2,
            email='jane_new@example.com',
            first_name='Jane'
        )
        if updated_user:
            print(f"Updated: {updated_user}")
            print(f"New email: {updated_user.email}\n")
        
        # Update by username
        print("Updating user 'bob_wilson' last_name:")
        updated_user = crud.update_user_by_username(
            username='bob_wilson',
            last_name='Wilson-Updated'
        )
        if updated_user:
            print(f"Updated: {updated_user}\n")
        
        # Deactivate user
        print("Deactivating user (ID: 3):")
        deactivated = crud.deactivate_user(3)
        if deactivated:
            print(f"User active status: {deactivated.is_active}\n")
        
        # Activate user
        print("Reactivating user (ID: 3):")
        activated = crud.activate_user(3)
        if activated:
            print(f"User active status: {activated.is_active}\n")
        
        # ===== DELETE OPERATIONS =====
        print("\n--- DELETE OPERATIONS ---\n")
        
        # Create user to delete
        print("Creating user for deletion:")
        delete_user = crud.create_user(
            username='temp_user',
            email='temp@example.com',
            password_hash=hash_password('temp123')
        )
        print(f"Created: {delete_user}")
        
        # Delete by ID
        print("Deleting user by ID:")
        deleted = crud.delete_user(delete_user.id)
        print(f"Deleted: {deleted}\n")
        
        # Create another user to delete by username
        print("Creating another user for deletion:")
        delete_user2 = crud.create_user(
            username='another_temp',
            email='temp2@example.com',
            password_hash=hash_password('temp456')
        )
        
        # Delete by username
        print("Deleting user by username:")
        deleted = crud.delete_user_by_username('another_temp')
        print(f"Deleted: {deleted}\n")
        
        # ===== FINAL SUMMARY =====
        print("\n--- FINAL SUMMARY ---\n")
        final_count = crud.count_users()
        print(f"Total users remaining: {final_count}")
        
        print("\nAll users in database:")
        final_users = crud.get_all_users(limit=20)
        for user in final_users:
            status = "Active" if user.is_active else "Inactive"
            print(f"  {user.id}. {user.username} ({user.email}) - {status}")
        
        # Display user as dictionary
        print("\nUser as dictionary (JSON format):")
        if final_users:
            print(final_users[0].to_dict())
        
    except Exception as e:
        print(f"Error: {str(e)}")
    
    finally:
        session.close()
        print("\n" + "="*60)
        print("Examples completed!")
        print("="*60 + "\n")


if __name__ == "__main__":
    main()
