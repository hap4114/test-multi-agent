```python
import bcrypt

# Initialize an empty dictionary to store user data
USERS_DB = {}

def register_user(email, password):
    # Convert the email to lowercase for case-insensitive comparison
    email = email.lower()
    
    # Check if the user already exists
    if email in USERS_DB:
        return "User already exists"
    
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Store the user data as a dictionary with the email and password hash
    USERS_DB[email] = {"email": email, "password": hashed_password}
    
    return "User created"

def get_user(email):
    # Convert the email to lowercase for case-insensitive comparison
    email = email.lower()
    
    # Get the user from the database
    user = USERS_DB.get(email)
    
    if user is None:
        return None
    else:
        return {"email": user["email"], "password": user["password"]}

def change_password(email, old_password, new_password):
    # Get the user from the database
    user = get_user(email)
    
    # Check if the user exists
    if user is None:
        return {"success": False, "error": "User not found"}
    
    # Check if the old password is correct
    if not bcrypt.checkpw(old_password.encode('utf-8'), user["password"]):
        return {"success": False, "error": "Wrong password"}
    
    # Hash the new password using bcrypt
    new_password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
    
    # Update the user's password
    user["password"] = new_password_hash
    USERS_DB[email] = user
    
    return {"success": True, "message": "Password changed!"}
```