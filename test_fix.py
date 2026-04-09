import pytest
from auth import register_user, get_user, change_password
import bcrypt

def test_register_user():
    # test register user
    result = register_user("test@example.com", "password123")
    assert result == "User created"

def test_register_user_already_exists():
    # test register user that already exists
    register_user("test@example.com", "password123")
    result = register_user("test@example.com", "password123")
    assert result == "User already exists"

def test_get_user():
    # test get user
    register_user("test@example.com", "password123")
    result = get_user("test@example.com")
    assert result is not None

def test_get_user_not_found():
    # test get user that does not exist
    result = get_user("test@example.com")
    assert result is None

def test_change_password():
    # test change password
    register_user("test@example.com", "password123")
    result = change_password("test@example.com", "password123", "newpassword123")
    assert result["success"] == True

def test_change_password_wrong_old_password():
    # test change password with wrong old password
    register_user("test@example.com", "password123")
    result = change_password("test@example.com", "wrongpassword123", "newpassword123")
    assert result["success"] == False

def test_change_password_user_not_found():
    # test change password for user that does not exist
    result = change_password("test@example.com", "password123", "newpassword123")
    assert result["success"] == False

def test_change_password_data_not_lost():
    # test change password does not lose user data
    register_user("test@example.com", "password123")
    user = get_user("test@example.com")
    change_password("test@example.com", "password123", "newpassword123")
    new_user = get_user("test@example.com")
    assert new_user["email"] == user["email"]

def test_change_password_password_updated():
    # test change password updates password
    register_user("test@example.com", "password123")
    change_password("test@example.com", "password123", "newpassword123")
    user = get_user("test@example.com")
    assert not bcrypt.checkpw("password123".encode('utf-8'), user["password"])
    assert bcrypt.checkpw("newpassword123".encode('utf-8'), user["password"])