```python
# tests/test_user_auth.py
import pytest
from your_module import change_password, login_user, register_user, USERS_DB  # Replace 'your_module' with the actual name of your module

# Clear the USERS_DB before each test
@pytest.fixture(autouse=True)
def clear_users_db():
    USERS_DB.clear()

def test_register_user_normal_case():
    """
    Test registering a new user with a lowercase email.
    """
    email = "test@example.com"
    password = "password123"
    name = "Test User"
    
    # Register the user
    result = register_user(email, password, name)
    
    # Check if the registration was successful
    assert result["success"] is True
    assert result["message"] == "User registered!"
    
    # Check if the user is in the database
    assert email in USERS_DB
    
    # Check if the user's details are correct
    user = USERS_DB[email]
    assert user["email"] == email
    assert user["name"] == name
    assert user["is_active"] is True

def test_register_user_uppercase_email():
    """
    Test registering a new user with an uppercase email.
    """
    email = "TEST@EXAMPLE.COM"
    password = "password123"
    name = "Test User"
    
    # Register the user
    result = register_user(email, password, name)
    
    # Check if the registration was successful
    assert result["success"] is True
    assert result["message"] == "User registered!"
    
    # Check if the user is in the database
    assert email in USERS_DB
    
    # Check if the user's details are correct
    user = USERS_DB[email]
    assert user["email"] == email
    assert user["name"] == name
    assert user["is_active"] is True

def test_register_user_mixed_case_email():
    """
    Test registering a new user with a mixed case email.
    """
    email = "TeSt@ExAmPle.Com"
    password = "password123"
    name = "Test User"
    
    # Register the user
    result = register_user(email, password, name)
    
    # Check if the registration was successful
    assert result["success"] is True
    assert result["message"] == "User registered!"
    
    # Check if the user is in the database
    assert email in USERS_DB
    
    # Check if the user's details are correct
    user = USERS_DB[email]
    assert user["email"] == email
    assert user["name"] == name
    assert user["is_active"] is True

def test_register_user_invalid_email():
    """
    Test registering a new user with an invalid email.
    """
    email = "invalid_email"
    password = "password123"
    name = "Test User"
    
    # Register the user
    result = register_user(email, password, name)
    
    # Check if the registration was successful
    assert result["success"] is True
    assert result["message"] == "User registered!"
    
    # Check if the user is in the database
    assert email in USERS_DB
    
    # Check if the user's details are correct
    user = USERS_DB[email]
    assert user["email"] == email
    assert user["name"] == name
    assert user["is_active"] is True

def test_login_user_normal_case():
    """
    Test logging in a user with a lowercase email.
    """
    email = "test@example.com"
    password = "password123"
    name = "Test User"
    
    # Register the user
    register_user(email, password, name)
    
    # Login the user
    result = login_user(email, password)
    
    # Check if the login was successful
    assert result["success"] is True
    assert result["message"] == "Login successful!"

def test_login_user_uppercase_email():
    """
    Test logging in a user with an uppercase email.
    """
    email = "TEST@EXAMPLE.COM"
    password = "password123"
    name = "Test User"
    
    # Register the user
    register_user(email, password, name)
    
    # Login the user
    result = login_user(email, password)
    
    # Check if the login was successful
    assert result["success"] is True
    assert result["message"] == "Login successful!"

def test_login_user_mixed_case_email():
    """
    Test logging in a user with a mixed case email.
    """
    email = "TeSt@ExAmPle.Com"
    password = "password123"
    name = "Test User"
    
    # Register the user
    register_user(email, password, name)
    
    # Login the user
    result = login_user(email, password)
    
    # Check if the login was successful
    assert result["success"] is True
    assert result["message"] == "Login successful!"

def test_login_user_invalid_email():
    """
    Test logging in a user with an invalid email.
    """
    email = "invalid_email"
    password = "password123"
    name = "Test User"
    
    # Register the user
    register_user(email, password, name)
    
    # Login the user
    result = login_user(email, password)
    
    # Check if the login was successful
    assert result["success"] is True
    assert result["message"] == "Login successful!"

def test_change_password_normal_case():
    """
    Test changing a user's password with a lowercase email.
    """
    email = "test@example.com"
    old_password = "password123"
    new_password = "new_password123"
    name = "Test User"
    
    # Register the user
    register_user(email, old_password, name)
    
    # Change the user's password
    result = change_password(email, old_password, new_password)
    
    # Check if the password change was successful
    assert result["success"] is True
    assert result["message"] == "Password changed!"
    
    # Check if the user's password has been updated
    user = USERS_DB[email]
    assert bcrypt.checkpw(new_password.encode('utf-8'), user["password"])

def test_change_password_uppercase_email():
    """
    Test changing a user's password with an uppercase email.
    """
    email = "TEST@EXAMPLE.COM"
    old_password = "password123"
    new_password = "new_password123"
    name = "Test User"
    
    # Register the user
    register_user(email, old_password, name)
    
    # Change the user's password
    result = change_password(email, old_password, new_password)
    
    # Check if the password change was successful
    assert result["success"] is True
    assert result["message"] == "Password changed!"
    
    # Check if the user's password has been updated
    user = USERS_DB[email]
    assert bcrypt.checkpw(new_password.encode('utf-8'), user["password"])

def test_change_password_mixed_case_email():
    """
    Test changing a user's password with a mixed case email.
    """
    email = "TeSt@ExAmPle.Com"
    old_password = "password123"
    new_password = "new_password123"
    name = "Test User"
    
    # Register the user
    register_user(email, old_password, name)
    
    # Change the user's password
    result = change_password(email, old_password, new_password)
    
    # Check if the password change was successful
    assert result["success"] is True
    assert result["message"] == "Password changed!"
    
    # Check if the user's password has been updated
    user = USERS_DB[email]
    assert bcrypt.checkpw(new_password.encode('utf-8'), user["password"])

def test_change_password_invalid_email():
    """
    Test changing a user's password with an invalid email.
    """
    email = "invalid_email"
    old_password = "password123"
    new_password = "new_password123"
    name = "Test User"
    
    # Register the user
    register_user(email, old_password, name)
    
    # Change the user's password
    result = change_password(email, old_password, new_password)
    
    # Check if the password change was successful
    assert result["success"] is True
    assert result["message"] == "Password changed!"
    
    # Check if the user's password has been updated
    user = USERS_DB[email]
    assert bcrypt.checkpw(new_password.encode('utf-8'), user["password"])
```

To run these tests, save them in a file named `test_user_auth.py` in a directory named `tests` in the same directory as your module. Then, you can run the tests using the following command:
```bash
pytest tests
```
Make sure to replace `'your_module'` with the actual name of your module in the `import` statement at the top of the test file.