```python
# Import the necessary libraries
from flask import request
import bcrypt
from datetime import datetime, timedelta

# Define the USERS_DB dictionary to store user information
USERS_DB = {}

# Define the BLOCKED_IPS set to store blocked IP addresses
BLOCKED_IPS = {}

# Define the LOGIN_ATTEMPTS dictionary to store login attempts
LOGIN_ATTEMPTS = {}

def login_user(email, password, ip_address='127.0.0.1'):
    # Convert the email to lowercase for case-insensitive comparison
    email = email.lower()
    
    # Get the user from the database
    user = USERS_DB.get(email)
    
    # Check if the user has exceeded the allowed number of login attempts
    if email in LOGIN_ATTEMPTS and ip_address in LOGIN_ATTEMPTS[email]:
        # Check if the user has exceeded the allowed number of login attempts within the last minute
        if LOGIN_ATTEMPTS[email][ip_address]['attempts'] >= 5 and (datetime.now() - LOGIN_ATTEMPTS[email][ip_address]['last_attempt']).total_seconds() < 60:
            return "Too many login attempts. Please try again later."
        else:
            # Increment the attempt count
            LOGIN_ATTEMPTS[email][ip_address]['attempts'] += 1
            LOGIN_ATTEMPTS[email][ip_address]['last_attempt'] = datetime.now()
    else:
        # Initialize the attempt count for the user and IP address
        if email not in LOGIN_ATTEMPTS:
            LOGIN_ATTEMPTS[email] = {}
        LOGIN_ATTEMPTS[email][ip_address] = {'attempts': 1, 'last_attempt': datetime.now()}
    
    # Check if the IP address has exceeded the allowed number of login attempts
    if ip_address in BLOCKED_IPS:
        # Check if the IP address has been blocked for more than 30 minutes
        if (datetime.now() - BLOCKED_IPS[ip_address]).total_seconds() > 1800:
            # Unblock the IP address
            del BLOCKED_IPS[ip_address]
        else:
            return "Your IP address has been blocked due to excessive login attempts."
    
    # Proceed with the login process
    if user is None:
        return "User not found"
    if not bcrypt.checkpw(password.encode('utf-8'), user):
        return "Invalid password"
    return "Login successful"

# Function to reset login attempts for a user and IP address
def reset_login_attempts(email, ip_address='127.0.0.1'):
    if email in LOGIN_ATTEMPTS and ip_address in LOGIN_ATTEMPTS[email]:
        LOGIN_ATTEMPTS[email][ip_address] = {'attempts': 0, 'last_attempt': datetime.now()}

# Function to block an IP address
def block_ip_address(ip_address):
    BLOCKED_IPS[ip_address] = datetime.now()
```