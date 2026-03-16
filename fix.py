### Fixed Code

The following code fixes the issue of storing passwords in plain text by using the bcrypt library for password hashing.

#### auth.py

```python
import bcrypt

def change_password(email, old_password, new_password):
    """
    Change user password
    
    Args:
        email (str): The email of the user.
        old_password (str): The old password of the user.
        new_password (str): The new password of the user.
    
    Returns:
        dict: A dictionary containing the result of the password change operation.
    """
    # Get the user from the database
    user = USERS_DB.get(email)
    
    # Check if the user exists
    if user is None:
        return {"success": False, "error": "User not found"}
    
    # Check if the old password is correct
    # Using bcrypt.checkpw to compare the input password with the hashed password stored in the database
    if not bcrypt.checkpw(old_password.encode('utf-8'), user["password"]):
        return {"success": False, "error": "Wrong password"}
    
    # Hash the new password using bcrypt
    # bcrypt.gensalt() generates a random salt for the password
    new_password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
    
    # Update the user's password
    user["password"] = new_password_hash
    
    return {"success": True, "message": "Password changed!"}

def login_user(email, password):
    """
    Login a user
    
    Args:
        email (str): The email of the user.
        password (str): The password of the user.
    
    Returns:
        dict: A dictionary containing the result of the login operation.
    """
    # Get the user from the database
    user = USERS_DB.get(email)
    
    # Check if the user exists
    if user is None:
        return {"success": False, "error": "User not found"}
    
    # Check if the password is correct
    # Using bcrypt.checkpw to compare the input password with the hashed password stored in the database
    if bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        return {"success": True, "message": "Login successful!"}
    else:
        return {"success": False, "error": "Wrong password"}
```

#### register_user.py

```python
import bcrypt

def register_user(email, password):
    """
    Register a new user
    
    Args:
        email (str): The email of the user.
        password (str): The password of the user.
    
    Returns:
        dict: A dictionary containing the result of the registration operation.
    """
    # Check if the user already exists
    if email in USERS_DB:
        return {"success": False, "error": "User already exists"}
    
    # Hash the password using bcrypt
    # bcrypt.gensalt() generates a random salt for the password
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Create a new user
    user = {
        "email": email,
        "password": password_hash
    }
    
    # Add the user to the database
    USERS_DB[email] = user
    
    return {"success": True, "message": "User registered successfully!"}
```

### Explanation of Changes

The following changes were made to fix the issue:

1.  **Installed the bcrypt library**: The bcrypt library was installed using pip to provide password hashing functionality.
2.  **Imported the bcrypt library**: The bcrypt library was imported in the `auth.py` and `register_user.py` files to use its functions.
3.  **Updated the `change_password` function**: The `change_password` function was updated to hash the new password using bcrypt before storing it in the database.
4.  **Updated the `login_user` function**: The `login_user` function was updated to use `bcrypt.checkpw` to compare the input password with the hashed password stored in the database.
5.  **Updated the `register_user` function**: The `register_user` function was updated to hash the password using bcrypt before storing it in the database.

These changes ensure that passwords are stored securely in the database, reducing the risk of password compromise in case of a database breach.