import bcrypt
import os

USERS_DB = {}

def register_user(email, password):
    email = email.lower()
    if email in USERS_DB:
        return "User already exists"
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    USERS_DB[email] = hashed_password
    return "User created"

def login_user(email, password):
    email = email.lower()
    user = USERS_DB.get(email)
    if user is None:
        return "User not found"
    if not bcrypt.checkpw(password.encode('utf-8'), user):
        return "Invalid password"
    return "Login successful"