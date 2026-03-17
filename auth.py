```python
USERS_DB = {}

def login_user(email, password):
    email = email.lower()
    user = USERS_DB.get(email)
    
    if user is None:
        return "User not found"
    
    if user["password"] != password:
        return "Invalid password"
    
    return "Login successful"

def register_user(email, password):
    email = email.lower()
    if email in USERS_DB:
        return "User already exists"
    
    USERS_DB[email] = {"password": password}
    return "User created"

def validate_email(email):
    email = email.lower()
    if "@" not in email:
        return "Invalid email"
    
    return "Email is valid"

def main():
    register_user("Test@Email.com", "password123")
    print(login_user("test@email.com", "password123"))  

if __name__ == "__main__":
    main()
```