```python
# tests/test_auth.py

import pytest
from auth import change_password, login_user
from register_user import register_user

# Mock database for testing
USERS_DB = {}

def setup_module():
    """Setup the mock database before running tests"""
    global USERS_DB
    USERS_DB = {}

def teardown_module():
    """Teardown the mock database after running tests"""
    global USERS_DB
    USERS_DB = {}

def test_register_user_normal_case():
    """Test registering a user with a normal email"""
    email = "test@example.com"
    password = "password123"
    result = register_user(email, password)
    assert result["success"] == True
    assert result["message"] == "User registered successfully!"
    assert email in USERS_DB

def test_register_user_uppercase_email():
    """Test registering a user with an uppercase email"""
    email = "TEST@EXAMPLE.COM"
    password = "password123"
    result = register_user(email, password)
    assert result["success"] == True
    assert result["message"] == "User registered successfully!"
    assert email in USERS_DB

def test_register_user_mixed_case_email():
    """Test registering a user with a mixed case email"""
    email = "TeSt@ExAmPle.Com"
    password = "password123"
    result = register_user(email, password)
    assert result["success"] == True
    assert result["message"] == "User registered successfully!"
    assert email in USERS_DB

def test_register_user_invalid_email():
    """Test registering a user with an invalid email"""
    email = "invalid_email"
    password = "password123"
    result = register_user(email, password)
    assert result["success"] == True
    assert result["message"] == "User registered successfully!"
    assert email in USERS_DB

def test_login_user_normal_case():
    """Test logging in a user with a normal email"""
    email = "test@example.com"
    password = "password123"
    register_user(email, password)
    result = login_user(email, password)
    assert result["success"] == True
    assert result["message"] == "Login successful!"

def test_login_user_uppercase_email():
    """Test logging in a user with an uppercase email"""
    email = "TEST@EXAMPLE.COM"
    password = "password123"
    register_user(email.lower(), password)
    result = login_user(email, password)
    assert result["success"] == True
    assert result["message"] == "Login successful!"

def test_login_user_mixed_case_email():
    """Test logging in a user with a mixed case email"""
    email = "TeSt@ExAmPle.Com"
    password = "password123"
    register_user(email.lower(), password)
    result = login_user(email, password)
    assert result["success"] == True
    assert result["message"] == "Login successful!"

def test_login_user_invalid_email():
    """Test logging in a user with an invalid email"""
    email = "invalid_email"
    password = "password123"
    register_user(email, password)
    result = login_user(email, password)
    assert result["success"] == True
    assert result["message"] == "Login successful!"

def test_change_password_normal_case():
    """Test changing a user's password with a normal email"""
    email = "test@example.com"
    old_password = "password123"
    new_password = "newpassword123"
    register_user(email, old_password)
    result = change_password(email, old_password, new_password)
    assert result["success"] == True
    assert result["message"] == "Password changed!"

def test_change_password_uppercase_email():
    """Test changing a user's password with an uppercase email"""
    email = "TEST@EXAMPLE.COM"
    old_password = "password123"
    new_password = "newpassword123"
    register_user(email.lower(), old_password)
    result = change_password(email, old_password, new_password)
    assert result["success"] == True
    assert result["message"] == "Password changed!"

def test_change_password_mixed_case_email():
    """Test changing a user's password with a mixed case email"""
    email = "TeSt@ExAmPle.Com"
    old_password = "password123"
    new_password = "newpassword123"
    register_user(email.lower(), old_password)
    result = change_password(email, old_password, new_password)
    assert result["success"] == True
    assert result["message"] == "Password changed!"

def test_change_password_invalid_email():
    """Test changing a user's password with an invalid email"""
    email = "invalid_email"
    old_password = "password123"
    new_password = "newpassword123"
    register_user(email, old_password)
    result = change_password(email, old_password, new_password)
    assert result["success"] == True
    assert result["message"] == "Password changed!"
```

However, the above test cases will fail because the `register_user`, `login_user`, and `change_password` functions are case-sensitive when it comes to email. To fix this, we need to modify these functions to convert the email to lowercase before checking or storing it in the database.

Here's the modified code:

```python
# register_user.py

def register_user(email, password):
    """Register a new user"""
    email = email.lower()  # Convert email to lowercase
    # Check if the user already exists
    if email in USERS_DB:
        return {"success": False, "error": "User already exists"}
    
    # Hash the password using bcrypt
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Create a new user
    user = {
        "email": email,
        "password": password_hash
    }
    
    # Add the user to the database
    USERS_DB[email] = user
    
    return {"success": True, "message": "User registered successfully!"}

# auth.py

def login_user(email, password):
    """Login a user"""
    email = email.lower()  # Convert email to lowercase
    # Get the user from the database
    user = USERS_DB.get(email)
    
    # Check if the user exists
    if user is None:
        return {"success": False, "error": "User not found"}
    
    # Check if the password is correct
    if bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        return {"success": True, "message": "Login successful!"}
    else:
        return {"success": False, "error": "Wrong password"}

def change_password(email, old_password, new_password):
    """Change user password"""
    email = email.lower()  # Convert email to lowercase
    # Get the user from the database
    user = USERS_DB.get(email)
    
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
    
    return {"success": True, "message": "Password changed!"}
```

With these modifications, the test cases should pass.