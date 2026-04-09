import pytest
from auth import register_user, login_user, USERS_DB
import bcrypt

def test_register_user():
    # test register user
    result = register_user("test@example.com", "password123")
    assert result == "User created"
    # check if user is in database
    assert "test@example.com" in USERS_DB

def test_register_user_already_exists():
    # test register user that already exists
    register_user("test@example.com", "password123")
    result = register_user("test@example.com", "password123")
    assert result == "User already exists"

def test_login_user():
    # test login user
    register_user("test@example.com", "password123")
    result = login_user("test@example.com", "password123")
    assert result == "Login successful"

def test_login_user_invalid_password():
    # test login user with invalid password
    register_user("test@example.com", "password123")
    result = login_user("test@example.com", "wrongpassword")
    assert result == "Invalid password"

def test_login_user_user_not_found():
    # test login user that does not exist
    result = login_user("test@example.com", "password123")
    assert result == "User not found"

def test_register_user_email_case_insensitive():
    # test register user with different email case
    register_user("TEST@EXAMPLE.COM", "password123")
    result = login_user("test@example.com", "password123")
    assert result == "Login successful"

def test_login_user_email_case_insensitive():
    # test login user with different email case
    register_user("test@example.com", "password123")
    result = login_user("TEST@EXAMPLE.COM", "password123")
    assert result == "Login successful"

def test_password_hashing():
    # test password hashing
    password = "password123"
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    assert bcrypt.checkpw(password.encode('utf-8'), hashed_password)

def test_password_hashing_different_passwords():
    # test password hashing with different passwords
    password1 = "password123"
    password2 = "wrongpassword"
    hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
    assert not bcrypt.checkpw(password2.encode('utf-8'), hashed_password)