```python
# Import the required libraries
import re

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
    return authenticateUser(user, password)

# Example usage:
if __name__ == "__main__":
    email = "Example@example.com"
    password = "password123"
    
    # Attempt to login with the provided credentials
    if loginUser(email, password):
        print("Login successful")
    else:
        print("Login failed")
```

**Changes Made:**

1.  **Email Validation Function (`isEmailValid`):**
    *   Added the `re.IGNORECASE` flag to the `re.match()` function to make the email format validation case-insensitive.
2.  **Database Query Function (`getUserByEmail`):**
    *   Modified the SQL query to use the `LOWER()` function to convert both the stored email address and the input email address to lowercase, ensuring a case-insensitive comparison.
3.  **Authentication Function (`loginUser`):**
    *   Changed the comparison of the email address to the stored email address to use the `lower()` method, ensuring a case-insensitive comparison.

**Why These Changes Were Made:**

*   The original code did not handle email addresses with uppercase letters correctly, resulting in failed logins.
*   By making the email validation and database query functions case-insensitive, we ensure that email addresses are treated consistently, regardless of case.
*   The changes to the authentication function ensure that the comparison of email addresses is also case-insensitive, allowing for successful logins even when the email address contains uppercase letters.