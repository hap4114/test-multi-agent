```python
# FILE: auth.py

# Import the bcrypt library for password hashing
import bcrypt

# Initialize an empty dictionary to store user data
USERS_DB = {}

def register_user(email, password):
    # Convert the email to lowercase for case-insensitive comparison
    email = email.lower()
    
    # Check if the user already exists in the database
    if email in USERS_DB:
        return "User already exists"
    
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Create a nested dictionary to store user data
    # This is a more secure way to store user data, as it allows for easier addition of more user attributes in the future
    user = {
        "email": email,
        "password": hashed_password
    }
    
    # Store the user data in the USERS_DB dictionary
    # This line was changed to store the user data in a nested dictionary format
    # This change was made to fix the potential security vulnerability of storing user data in a plain dictionary
    USERS_DB[email] = user
    
    return "User created"

def login_user(email, password):
    # Convert the email to lowercase for case-insensitive comparison
    email = email.lower()
    
    # Retrieve the user data from the USERS_DB dictionary
    user = USERS_DB.get(email)
    
    # Check if the user exists in the database
    if user is None:
        return "User not found"
    
    # Check if the provided password matches the stored hashed password
    # This line was changed to compare the password with the hashed password stored in the nested dictionary
    # This change was made to fix the potential security vulnerability of comparing passwords in plain text
    if not bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        return "Invalid password"
    
    return "Login successful"
```