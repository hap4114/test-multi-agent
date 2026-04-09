import pytest
from auth import login_user, USERS_DB, LOGIN_ATTEMPTS, BLOCKED_IPS, reset_login_attempts, block_ip_address
import bcrypt

@pytest.fixture(autouse=True)
def clear_state():
    USERS_DB.clear()
    LOGIN_ATTEMPTS.clear()
    BLOCKED_IPS.clear()
    yield
    USERS_DB.clear()
    LOGIN_ATTEMPTS.clear()
    BLOCKED_IPS.clear()

def test_normal_case():
    # test normal login
    USERS_DB['user@example.com'] = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt())
    result = login_user('user@example.com', 'password')
    assert result == "Login successful"

def test_uppercase_email():
    # test login with uppercase email
    USERS_DB['user@example.com'] = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt())
    result = login_user('USER@EXAMPLE.COM', 'password')
    assert result == "Login successful"

def test_invalid_password():
    # test login with invalid password
    USERS_DB['user@example.com'] = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt())
    result = login_user('user@example.com', 'wrongpassword')
    assert result == "Invalid password"

def test_user_not_found():
    # test login with non-existent user
    result = login_user('user@example.com', 'password')
    assert result == "User not found"

def test_rate_limiting():
    # test rate limiting
    USERS_DB['user@example.com'] = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt())
    for _ in range(5):
        login_user('user@example.com', 'wrongpassword')
    result = login_user('user@example.com', 'wrongpassword')
    assert result == "Too many login attempts. Please try again later."

def test_ip_blocking():
    # test IP blocking
    USERS_DB['user@example.com'] = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt())
    for _ in range(5):
        login_user('user@example.com', 'wrongpassword')
    block_ip_address('127.0.0.1')
    result = login_user('user@example.com', 'password')
    assert result == "Your IP address has been blocked due to excessive login attempts."

def test_reset_login_attempts():
    # test reset login attempts
    USERS_DB['user@example.com'] = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt())
    for _ in range(5):
        login_user('user@example.com', 'wrongpassword')
    reset_login_attempts('user@example.com', '127.0.0.1')
    result = login_user('user@example.com', 'wrongpassword')
    assert result != "Too many login attempts. Please try again later."

def test_block_ip_address():
    # test block IP address
    USERS_DB['user@example.com'] = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt())
    block_ip_address('127.0.0.1')
    result = login_user('user@example.com', 'password')
    assert result == "Your IP address has been blocked due to excessive login attempts."