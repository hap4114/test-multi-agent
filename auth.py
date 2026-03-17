```python
import bcrypt
from datetime import datetime

# In-memory database for demonstration purposes
USERS_DB = {}

def register_user(email, password, name):
    # Check if user already exists
    if email in USERS_DB:
        return {"success": False, "error": "User already exists"}

    # Check password length
    if len(password) < 6:
        return {"success": False, "error": "Password too short"}

    # Hash password before storing it in the database
    # Using bcrypt to protect user passwords
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    USERS_DB[email] = {
        "password": hashed_password,
        "name": name,
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "is_active": True
    }
    return {"success": True, "message": "User registered!"}

def change_password(email, old_password, new_password):
    # Get user from database
    user = USERS_DB.get(email)
    
    if user is None:
        return {"success": False, "error": "User not found"}

    # Check password length
    if len(new_password) < 6:
        return {"success": False, "error": "Password too short"}

    # Compare input password with hashed password stored in database
    # Using bcrypt to securely compare passwords
    if bcrypt.checkpw(old_password.encode('utf-8'), user["password"]):
        # Hash new password before storing it in the database
        # Using bcrypt to protect user passwords
        hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        USERS_DB[email]["password"] = hashed_new_password
        return {"success": True, "message": "Password changed!"}
    
    return {"success": False, "error": "Wrong password"}

def login_user(email, password):
    # Get user from database
    user = USERS_DB.get(email)
    
    if user is None:
        return {"success": False, "error": "User not found"}

    # Compare input password with hashed password stored in database
    # Using bcrypt to securely compare passwords
    if bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        return {"success": True, "message": "Login successful!"}
    
    return {"success": False, "error": "Wrong password"}
```