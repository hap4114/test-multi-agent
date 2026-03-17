```python
# tests/test_login.py
import pytest
from your_module import login_user, register_user, validate_email, USERS_DB  # Replace 'your_module' with the actual module name

# Initialize an empty USERS_DB for each test
@pytest.fixture(autouse=True)
def reset_users_db():
    global USERS_DB
    USERS_DB = {}

def test_normal_case():
    # Test normal case with lowercase email
    register_user("test@email.com", "password123")
    assert login_user("test@email.com", "password123") == "Login successful"

def test_uppercase_email():
    # Test uppercase email
    register_user("TEST@EMAIL.COM", "password123")
    assert login_user("TEST@EMAIL.COM", "password123") == "Login successful"

def test_mixed_case_email():
    # Test mixed case email
    register_user("TeSt@EmAiL.cOm", "password123")
    assert login_user("TeSt@EmAiL.cOm", "password123") == "Login successful"

def test_invalid_email():
    # Test invalid email
    assert validate_email("invalid_email") == "Invalid email"

def test_invalid_credentials():
    # Test invalid credentials
    register_user("test@email.com", "password123")
    assert login_user("test@email.com", "wrong_password") == "Invalid password"

def test_user_not_found():
    # Test user not found
    assert login_user("non_existent_user@email.com", "password123") == "User not found"

def test_user_already_exists():
    # Test user already exists
    register_user("test@email.com", "password123")
    assert register_user("test@email.com", "password123") == "User already exists"

def test_case_insensitive_login():
    # Test case insensitive login
    register_user("test@email.com", "password123")
    assert login_user("TEST@EMAIL.COM", "password123") == "Login successful"
    assert login_user("tEsT@eMaIl.cOm", "password123") == "Login successful"
```

To run these tests, save this code in a file named `test_login.py` and use the following command:
```bash
pytest test_login.py
```
Make sure to replace `'your_module'` with the actual module name where the `login_user`, `register_user`, `validate_email`, and `USERS_DB` are defined.

Note: The `reset_users_db` fixture is used to reset the `USERS_DB` for each test, ensuring that each test starts with a clean database.