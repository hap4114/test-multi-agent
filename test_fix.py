Here's a complete, runnable pytest code for the given scenarios:

```python
# tests/test_fix.py
import pytest
from auth import register_user, login_user, change_password
import bcrypt

# Test data
valid_email = "user@example.com"
valid_password = "password123"
valid_name = "John Doe"
invalid_email = "invalid_email"
invalid_password = "wrong_password"

def test_register_user_normal_case():
    """
    Test registering a new user with a normal email address.
    """
    register_user(valid_email, valid_password, valid_name)
    assert valid_email in register_user.__globals__["USERS_DB"]
    assert bcrypt.checkpw(valid_password.encode('utf-8'), register_user.__globals__["USERS_DB"][valid_email]["password"])

def test_register_user_uppercase_email():
    """
    Test registering a new user with an uppercase email address.
    """
    uppercase_email = valid_email.upper()
    register_user(uppercase_email, valid_password, valid_name)
    assert uppercase_email in register_user.__globals__["USERS_DB"]
    assert bcrypt.checkpw(valid_password.encode('utf-8'), register_user.__globals__["USERS_DB"][uppercase_email]["password"])

def test_register_user_mixed_case_email():
    """
    Test registering a new user with a mixed case email address.
    """
    mixed_case_email = valid_email.capitalize()
    register_user(mixed_case_email, valid_password, valid_name)
    assert mixed_case_email in register_user.__globals__["USERS_DB"]
    assert bcrypt.checkpw(valid_password.encode('utf-8'), register_user.__globals__["USERS_DB"][mixed_case_email]["password"])

def test_register_user_invalid_email():
    """
    Test registering a new user with an invalid email address.
    """
    register_user(invalid_email, valid_password, valid_name)
    assert invalid_email in register_user.__globals__["USERS_DB"]
    assert bcrypt.checkpw(valid_password.encode('utf-8'), register_user.__globals__["USERS_DB"][invalid_email]["password"])

def test_login_user_normal_case():
    """
    Test logging in a user with a normal email address.
    """
    register_user(valid_email, valid_password, valid_name)
    result = login_user(valid_email, valid_password)
    assert result["success"] is True
    assert result["user"] == valid_name

def test_login_user_uppercase_email():
    """
    Test logging in a user with an uppercase email address.
    """
    uppercase_email = valid_email.upper()
    register_user(uppercase_email, valid_password, valid_name)
    result = login_user(uppercase_email, valid_password)
    assert result["success"] is True
    assert result["user"] == valid_name

def test_login_user_mixed_case_email():
    """
    Test logging in a user with a mixed case email address.
    """
    mixed_case_email = valid_email.capitalize()
    register_user(mixed_case_email, valid_password, valid_name)
    result = login_user(mixed_case_email, valid_password)
    assert result["success"] is True
    assert result["user"] == valid_name

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
    result = login_user(valid_email, invalid_password)
    assert result["success"] is False
    assert result["error"] == "Wrong password"

def test_change_password_normal_case():
    """
    Test changing a user's password with a normal email address.
    """
    register_user(valid_email, valid_password, valid_name)
    new_password = "newpassword123"
    result = change_password(valid_email, valid_password, new_password)
    assert result["success"] is True
    assert bcrypt.checkpw(new_password.encode('utf-8'), register_user.__globals__["USERS_DB"][valid_email]["password"])

def test_change_password_uppercase_email():
    """
    Test changing a user's password with an uppercase email address.
    """
    uppercase_email = valid_email.upper()
    register_user(uppercase_email, valid_password, valid_name)
    new_password = "newpassword123"
    result = change_password(uppercase_email, valid_password, new_password)
    assert result["success"] is True
    assert bcrypt.checkpw(new_password.encode('utf-8'), register_user.__globals__["USERS_DB"][uppercase_email]["password"])

def test_change_password_mixed_case_email():
    """
    Test changing a user's password with a mixed case email address.
    """
    mixed_case_email = valid_email.capitalize()
    register_user(mixed_case_email, valid_password, valid_name)
    new_password = "newpassword123"
    result = change_password(mixed_case_email, valid_password, new_password)
    assert result["success"] is True
    assert bcrypt.checkpw(new_password.encode('utf-8'), register_user.__globals__["USERS_DB"][mixed_case_email]["password"])

def test_change_password_invalid_email():
    """
    Test changing a user's password with an invalid email address.
    """
    result = change_password(invalid_email, valid_password, "newpassword123")
    assert result["success"] is False
    assert result["error"] == "User not found"

def test_change_password_wrong_old_password():
    """
    Test changing a user's password with a wrong old password.
    """
    register_user(valid_email, valid_password, valid_name)
    new_password = "newpassword123"
    result = change_password(valid_email, invalid_password, new_password)
    assert result["success"] is False
    assert result["error"] == "Wrong password"
```

To run these tests, save the above code in a file named `test_fix.py` and the provided code fix in a file named `auth.py`. Then, navigate to the directory containing these files and run the following command:

```bash
pytest test_fix.py
```

This will execute all the test cases and report any failures or errors.