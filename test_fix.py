```python
# tests/test_auth.py

import pytest
from auth import login_user, register_user, get_user, USERS_DB

# Clear the users database before each test
@pytest.fixture(autouse=True)
def clear_users_db():
    USERS_DB.clear()

def test_normal_case():
    """
    Test that a user can login with a lowercase email
    """
    # Register a new user
    register_user('test@example.com', 'password123')
    
    # Try logging in with the same email
    assert login_user('test@example.com', 'password123') == True

def test_uppercase_email():
    """
    Test that a user can login with an uppercase email
    """
    # Register a new user
    register_user('test@example.com', 'password123')
    
    # Try logging in with an uppercase email
    assert login_user('TEST@EXAMPLE.COM', 'password123') == True

def test_mixed_case_email():
    """
    Test that a user can login with a mixed case email
    """
    # Register a new user
    register_user('test@example.com', 'password123')
    
    # Try logging in with a mixed case email
    assert login_user('TeSt@ExAmPle.Com', 'password123') == True

def test_invalid_email():
    """
    Test that an invalid email fails to login
    """
    # Register a new user
    register_user('test@example.com', 'password123')
    
    # Try logging in with an invalid email
    assert login_user('invalid@example.com', 'password123') == False

def test_invalid_password():
    """
    Test that an invalid password fails to login
    """
    # Register a new user
    register_user('test@example.com', 'password123')
    
    # Try logging in with an invalid password
    assert login_user('test@example.com', 'wrongpassword') == False

def test_get_user():
    """
    Test that the get_user function returns the correct user
    """
    # Register a new user
    register_user('test@example.com', 'password123')
    
    # Get the user
    user = get_user('test@example.com')
    
    # Check that the user exists and has the correct password
    assert user is not None
    assert user['password'] == 'password123'

def test_register_user():
    """
    Test that the register_user function registers a new user
    """
    # Register a new user
    assert register_user('test@example.com', 'password123') == True
    
    # Try registering the same user again
    assert register_user('test@example.com', 'password123') == False
```

To run these tests, save the test code in a file named `test_auth.py` and the fixed code in a file named `auth.py`. Then, navigate to the directory containing the files and run the following command:
```bash
pytest test_auth.py
```
This will run all the tests and report any failures or errors.