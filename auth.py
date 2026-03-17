```python
# auth.py

# Define a dictionary to store users in memory for simplicity
# In a real application, this would be replaced with a database
USERS_DB = {}

def login_user(email, password):
    """
    Login a user with email and password
    """
    # Convert email to lowercase to ensure case-insensitive comparison
    # This fixes the bug where login fails when email contains uppercase letters
    email = email.lower()  
    user = USERS_DB.get(email)
    
    # Check if user exists and password is correct
    if user and user['password'] == password:
        return True
    else:
        return False

def register_user(email, password):
    """
    Register a new user
    """
    # Convert email to lowercase to ensure case-insensitive comparison
    # This ensures that emails are stored in a consistent case
    email = email.lower()  
    if email in USERS_DB:
        return False  # User already exists
    else:
        USERS_DB[email] = {'password': password}
        return True

def get_user(email):
    """
    Get a user by email
    """
    # Convert email to lowercase to ensure case-insensitive comparison
    email = email.lower()  
    return USERS_DB.get(email)

# Example usage:
if __name__ == "__main__":
    register_user('test@example.com', 'password123')
    print(login_user('Test@Example.com', 'password123'))  # Should print: True
    print(login_user('test@example.com', 'wrongpassword'))  # Should print: False
```