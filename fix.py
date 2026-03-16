```python
# Modified authenticateUser function to ensure case-insensitive comparison
def authenticateUser(email, password):
    # Get the user by email in a case-insensitive manner
    user = getUserByEmail(email.lower())
    
    # Check if the user exists and the password is correct
    if user and user.password == password:
        return True
    else:
        return False

# Modified getUserByEmail function to convert the email parameter to lowercase
def getUserByEmail(email):
    # Define the SQL query to get the user by email
    query = "SELECT * FROM users WHERE LOWER(email) = LOWER(%s)"
    
    # Execute the query with the email parameter converted to lowercase
    return db.query(query, (email.lower(),))

# Modified loginUser function to use the updated authenticateUser and getUserByEmail functions
def loginUser(email, password):
    # Authenticate the user in a case-insensitive manner
    if authenticateUser(email.lower(), password):
        # Get the user by email in a case-insensitive manner
        user = getUserByEmail(email.lower())
        
        # Return the user if authentication is successful
        return user
    else:
        # Return None if authentication fails
        return None

# The isEmailValid function remains unchanged as it is already case-insensitive
def isEmailValid(email):
    # Define the regular expression pattern for email validation
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    # Use the re.IGNORECASE flag to make the pattern case-insensitive
    if re.match(pattern, email, re.IGNORECASE):
        return True
    else:
        return False

# Example usage:
email = "Test@Email.com"
password = "password123"

# Validate the email address
if isEmailValid(email):
    # Attempt to login the user
    user = loginUser(email, password)
    
    # Check if the login is successful
    if user:
        print("Login successful")
    else:
        print("Invalid credentials")
else:
    print("Invalid email address")
```

**Changes:**

1.  **Case-insensitive comparison**: The `authenticateUser` function now uses the `lower()` method to convert the email address to lowercase before comparison, ensuring a case-insensitive comparison.
2.  **Convert email to lowercase**: The `getUserByEmail` function now converts the `email` parameter to lowercase using the `lower()` method before passing it to the SQL query, ensuring consistency and case-insensitivity.
3.  **Updated loginUser function**: The `loginUser` function now uses the updated `authenticateUser` and `getUserByEmail` functions to ensure case-insensitive comparison and email conversion to lowercase.

**Why these changes were made:**

*   The changes were made to address the issue of user login failing when the email address contains uppercase letters.
*   By ensuring case-insensitive comparison in the `authenticateUser` function and converting the email parameter to lowercase in the `getUserByEmail` function, we can guarantee that the login process works correctly regardless of the case used in the email address.
*   The updated `loginUser` function now uses the modified `authenticateUser` and `getUserByEmail` functions to provide a seamless and case-insensitive login experience.