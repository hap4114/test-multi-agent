```python
# tests/test_user_auth.py

import pytest
from your_module import register_user, change_password, login_user  # Replace 'your_module' with the actual name of your module

# Test data
valid_email = "test@example.com"
valid_password = "password123"
valid_name = "Test User"

invalid_email = "invalid_email"
short_password = "short"

def test_register_user_normal_case():
    """
    Test registering a user with a normal email address.
    """
    result = register_user(valid_email, valid_password, valid_name)
    assert result["success"] is True
    assert result["message"] == "User registered!"

def test_register_user_uppercase_email():
    """
    Test registering a user with an uppercase email address.
    """
    result = register_user(valid_email.upper(), valid_password, valid_name)
    assert result["success"] is False
    assert result["error"] == "User already exists"

def test_register_user_mixed_case_email():
    """
    Test registering a user with a mixed case email address.
    """
    result = register_user(valid_email.capitalize(), valid_password, valid_name)
    assert result["success"] is False
    assert result["error"] == "User already exists"

def test_register_user_invalid_email():
    """
    Test registering a user with an invalid email address.
    """
    result = register_user(invalid_email, valid_password, valid_name)
    assert result["success"] is True
    assert result["message"] == "User registered!"

def test_register_user_short_password():
    """
    Test registering a user with a short password.
    """
    result = register_user(valid_email, short_password, valid_name)
    assert result["success"] is False
    assert result["error"] == "Password too short"

def test_change_password_normal_case():
    """
    Test changing a user's password with a normal email address.
    """
    register_user(valid_email, valid_password, valid_name)
    result = change_password(valid_email, valid_password, "new_password")
    assert result["success"] is True
    assert result["message"] == "Password changed!"

def test_change_password_uppercase_email():
    """
    Test changing a user's password with an uppercase email address.
    """
    register_user(valid_email, valid_password, valid_name)
    result = change_password(valid_email.upper(), valid_password, "new_password")
    assert result["success"] is False
    assert result["error"] == "User not found"

def test_change_password_mixed_case_email():
    """
    Test changing a user's password with a mixed case email address.
    """
    register_user(valid_email, valid_password, valid_name)
    result = change_password(valid_email.capitalize(), valid_password, "new_password")
    assert result["success"] is False
    assert result["error"] == "User not found"

def test_change_password_invalid_email():
    """
    Test changing a user's password with an invalid email address.
    """
    result = change_password(invalid_email, valid_password, "new_password")
    assert result["success"] is False
    assert result["error"] == "User not found"

def test_login_user_normal_case():
    """
    Test logging in a user with a normal email address.
    """
    register_user(valid_email, valid_password, valid_name)
    result = login_user(valid_email, valid_password)
    assert result["success"] is True
    assert result["message"] == "Login successful!"

def test_login_user_uppercase_email():
    """
    Test logging in a user with an uppercase email address.
    """
    register_user(valid_email, valid_password, valid_name)
    result = login_user(valid_email.upper(), valid_password)
    assert result["success"] is False
    assert result["error"] == "User not found"

def test_login_user_mixed_case_email():
    """
    Test logging in a user with a mixed case email address.
    """
    register_user(valid_email, valid_password, valid_name)
    result = login_user(valid_email.capitalize(), valid_password)
    assert result["success"] is False
    assert result["error"] == "User not found"

def test_login_user_invalid_email():
    """
    Test logging in a user with an invalid email address.
    """
    result = login_user(invalid_email, valid_password)
    assert result["success"] is False
    assert result["error"] == "User not found"

def test_login_user_wrong_password():
    """
    Test logging in a user with a wrong password.
    """
    register_user(valid_email, valid_password, valid_name)
    result = login_user(valid_email, "wrong_password")
    assert result["success"] is False
    assert result["error"] == "Wrong password"
```

To run these tests, save this code in a file named `test_user_auth.py` and run `pytest` in your terminal. Make sure to replace `'your_module'` with the actual name of your module.

Note: These tests cover the scenarios you specified, but you may want to add more tests to cover additional scenarios, such as testing the `register_user` function with an empty email or password, or testing the `change_password` function with a new password that is too short.