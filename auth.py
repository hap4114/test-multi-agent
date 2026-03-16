# auth.py - User Authentication Module
# WARNING: This file has intentional bugs for testing!

import re
from datetime import datetime

# Fake database of users
USERS_DB = {
    "john@example.com": {
        "password": "password123",
        "name": "John Doe",
        "created_at": "2024-01-01",
        "is_active": True
    },
    "jane@example.com": {
        "password": "securepass",
        "name": "Jane Smith", 
        "created_at": "2024-01-02",
        "is_active": True
    }
}

# ============================================
# BUG 1: Case sensitivity in email login
# ============================================
def login_user(email, password):
    """Login a user with email and password"""
    # BUG: email is not converted to lowercase
    # so "John@Example.com" won't find "john@example.com"
    user = USERS_DB.get(email)
    
    if user is None:
        return {"success": False, "error": "User not found"}
    
    if user["password"] == password:
        return {"success": True, "user": user["name"]}
    
    return {"success": False, "error": "Wrong password"}


# ============================================
# BUG 2: Email validation is broken
# ============================================
def validate_email(email):
    """Check if email format is valid"""
    # BUG: this regex is wrong — it rejects valid emails
    # with dots in the username like "john.doe@example.com"
    pattern = r"^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$"
    return bool(re.match(pattern, email))


# ============================================
# BUG 3: Password check is case sensitive
# ============================================
def register_user(email, password, name):
    """Register a new user"""
    # BUG: no check if user already exists!
    # registering same email twice overwrites the old user
    
    if len(password) < 6:
        return {"success": False, "error": "Password too short"}
    
    USERS_DB[email] = {
        "password": password,
        "name": name,
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "is_active": True
    }
    return {"success": True, "message": "User registered!"}


# ============================================
# BUG 4: Division by zero possible
# ============================================
def get_login_stats():
    """Get login statistics"""
    total_users = len(USERS_DB)
    active_users = len([u for u in USERS_DB.values() if u["is_active"]])
    
    # BUG: if total_users is 0 this will crash!
    percentage = (active_users / total_users) * 100
    
    return {
        "total": total_users,
        "active": active_users,
        "percentage": percentage
    }


# ============================================
# BUG 5: Wrong comparison operator
# ============================================
def is_admin(email):
    """Check if user is an admin"""
    admin_emails = ["admin@example.com", "root@example.com"]
    
    # BUG: uses 'is' instead of 'in' for list check
    # 'is' checks identity not membership!
    return email is admin_emails


# ============================================
# BUG 6: Password stored in plain text
# ============================================
def change_password(email, old_password, new_password):
    """Change user password"""
    user = USERS_DB.get(email)
    
    if user is None:
        return {"success": False, "error": "User not found"}
    
    # BUG: passwords stored as plain text — security risk!
    if user["password"] == old_password:
        user["password"] = new_password
        return {"success": True, "message": "Password changed!"}
    
    return {"success": False, "error": "Wrong password"}
```

Click **"Commit new file"** ✅

---

## Step 2 — Create a matching GitHub Issue

Go to **Issues** → **New Issue**

**Title:**
```
Bug: Login fails with uppercase email and admin check always returns False
```

**Description:**
```
## Bugs Found in auth.py

**Bug 1 - Login case sensitivity:**
- Login with "John@Example.com" fails even though 
  "john@example.com" exists in the database

**Bug 2 - Email validation broken:**
- Valid emails like "john.doe@example.com" are 
  rejected by validate_email()

**Bug 3 - Duplicate registration:**
- register_user() doesn't check if email 
  already exists — overwrites existing users!

**Bug 4 - Division by zero:**
- get_login_stats() crashes if no users exist

**Bug 5 - Admin check broken:**
- is_admin() always returns False because 
  it uses 'is' instead of 'in'

Expected: All these functions should work correctly
