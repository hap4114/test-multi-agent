```python
import bcrypt
import datetime

# Define the USERS_DB dictionary to store user data
USERS_DB = {}

def register_user(email, password, name):
    """
    Register a new user
    """
    # Hash the password before storing it in the database
    # This is a security fix to prevent storing passwords in plain text
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Store the user data in the USERS_DB dictionary
    USERS_DB[email] = {
        "password": password_hash,  # Store the hashed password
        "name": name,
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d"),
        "is_active": True
    }

def login_user(email, password):
    """
    Login a user
    """
    # Check if the user exists in the database
    if email not in USERS_DB:
        return {"success": False, "error": "User not found"}
    
    # Get the user data from the database
    user = USERS_DB[email]
    
    # Compare the input password with the hashed password stored in the database
    # This is a security fix to prevent comparing passwords in plain text
    if bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        return {"success": True, "user": user["name"], "email": email}
    else:
        return {"success": False, "error": "Wrong password"}

def change_password(email, old_password, new_password):
    """
    Change user password
    """
    # Check if the user exists in the database
    if email not in USERS_DB:
        return {"success": False, "error": "User not found"}
    
    # Get the user data from the database
    user = USERS_DB[email]
    
    # Compare the old password with the hashed password stored in the database
    # This is a security fix to prevent comparing passwords in plain text
    if not bcrypt.checkpw(old_password.encode('utf-8'), user["password"]):
        return {"success": False, "error": "Wrong password"}
    
    # Hash the new password before storing it in the database
    # This is a security fix to prevent storing passwords in plain text
    new_password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
    
    # Update the user data with the new password
    USERS_DB[email]["password"] = new_password_hash
    
    return {"success": True, "user": user["name"], "email": email}

# Example usage:
if __name__ == "__main__":
    register_user("user@example.com", "password123", "John Doe")
    print(login_user("user@example.com", "password123"))
    print(change_password("user@example.com", "password123", "newpassword123"))
    print(login_user("user@example.com", "newpassword123"))
```