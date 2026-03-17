```python
import bcrypt
from datetime import datetime

USERS_DB = {}

def change_password(email, old_password, new_password):
    user = USERS_DB.get(email)
    
    if user is None:
        return {"success": False, "error": "User not found"}
    
    if not bcrypt.checkpw(old_password.encode('utf-8'), user["password"]):
        return {"success": False, "error": "Wrong password"}
    
    new_password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
    
    user["password"] = new_password_hash
    
    USERS_DB[email] = user
    
    return {"success": True, "message": "Password changed!"}

def login_user(email, password):
    user = USERS_DB.get(email)
    
    if user is None:
        return {"success": False, "error": "User not found"}
    
    if bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        return {"success": True, "message": "Login successful!"}
    else:
        return {"success": False, "error": "Wrong password"}

def register_user(email, password, name):
    if email in USERS_DB:
        return {"success": False, "error": "User already exists"}
    
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    user = {
        "email": email,
        "password": password_hash,
        "name": name,
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "is_active": True
    }
    
    USERS_DB[email] = user
    
    return {"success": True, "message": "User registered!"}
```