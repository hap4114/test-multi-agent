```python
# Import the required libraries
import pytest
import re
from unittest.mock import Mock

# Email validation function
def isEmailValid(email):
    """
    Validate the format of an email address.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    # Regular expression to validate email format (case-insensitive)
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    # Use re.IGNORECASE flag to make the validation case-insensitive
    return re.match(pattern, email, re.IGNORECASE) is not None

# Database query function
def getUserByEmail(email):
    """
    Retrieve a user from the database by their email address.
    
    Args:
        email (str): The email address to search for.
    
    Returns:
        object: The user object if found, None otherwise.
    """
    # Mock database query for testing purposes
    db = Mock()
    db.query.return_value = Mock(email="example@example.com")
    # SQL query to retrieve user data (case-insensitive)
    query = "SELECT * FROM users WHERE LOWER(email) = LOWER(%s)"
    # Execute the query with the email address as a parameter
    return db.query(query, (email,))

# Authentication function
def loginUser(email, password):
    """
    Authenticate a user with their email address and password.
    
    Args:
        email (str): The email address to authenticate.
        password (str): The password to authenticate.
    
    Returns:
        bool: True if the authentication is successful, False otherwise.
    """
    # Validate email address
    if not isEmailValid(email):
        # If the email address is invalid, return False
        return False
    
    # Retrieve user data from database
    user = getUserByEmail(email)
    
    # Check if the user exists
    if user is None:
        # If the user does not exist, return False
        return False
    
    # Compare email address to stored email address (case-insensitive)
    if user.email.lower() != email.lower():
        # If the email addresses do not match, return False
        return False
    
    # Authenticate user
    return True  # Mock authentication for testing purposes

# Pytest test cases
def test_login_user_normal_case():
    """
    Test the login function with a normal email address (all lowercase).
    """
    email = "example@example.com"
    password = "password123"
    assert loginUser(email, password) == True

def test_login_user_uppercase_email():
    """
    Test the login function with an email address containing uppercase letters.
    """
    email = "Example@example.com"
    password = "password123"
    assert loginUser(email, password) == True

def test_login_user_mixed_case_email():
    """
    Test the login function with an email address containing a mix of uppercase and lowercase letters.
    """
    email = "ExAmPle@example.com"
    password = "password123"
    assert loginUser(email, password) == True

def test_login_user_invalid_email():
    """
    Test the login function with an invalid email address.
    """
    email = "invalid_email"
    password = "password123"
    assert loginUser(email, password) == False

def test_login_user_empty_email():
    """
    Test the login function with an empty email address.
    """
    email = ""
    password = "password123"
    assert loginUser(email, password) == False

def test_login_user_none_email():
    """
    Test the login function with a None email address.
    """
    email = None
    password = "password123"
    with pytest.raises(AttributeError):
        loginUser(email, password)

# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])
```

To run the tests, save the above code in a file (e.g., `test_login.py`) and execute the file using the `pytest` command:

```bash
pytest test_login.py
```

This will run all the test cases and report any failures or errors.