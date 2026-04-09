import pytest
from auth import login_user, register_user, USERS_DB

@pytest.fixture(autouse=True)
def clear_state():
    # Clear the USERS_DB dictionary before and after each test
    USERS_DB.clear()
    yield
    USERS_DB.clear()

def test_register_user():
    # Test registering a new user
    result = register_user("test@example.com", "password123")
    assert result == "User created"

def test_register_existing_user():
    # Test registering an existing user
    register_user("test@example.com", "password123")
    result = register_user("test@example.com", "password123")
    assert result == "User already exists"

def test_login_user():
    # Test logging in a registered user
    register_user("test@example.com", "password123")
    result = login_user("test@example.com", "password123")
    assert result == "Login successful"

def test_login_unregistered_user():
    # Test logging in an unregistered user
    result = login_user("test@example.com", "password123")
    assert result == "User not found"

def test_login_incorrect_password():
    # Test logging in with an incorrect password
    register_user("test@example.com", "password123")
    result = login_user("test@example.com", "wrongpassword")
    assert result == "Invalid password"

def test_login_case_insensitive_email():
    # Test logging in with a case-insensitive email
    register_user("test@example.com", "password123")
    result = login_user("TEST@EXAMPLE.COM", "password123")
    assert result == "Login successful"

def test_register_case_insensitive_email():
    # Test registering with a case-insensitive email
    register_user("test@example.com", "password123")
    result = register_user("TEST@EXAMPLE.COM", "password123")
    assert result == "User already exists"