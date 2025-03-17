"""
Simple banking system with some intentional SonarQube quality violations.
"""

import json
import hashlib

# Hardcoded credentials (Security issue)
USERS = {
    "user1": "5f4dcc3b5aa765d61d8327deb882cf99",  # Password: password (MD5 - insecure hashing)
    "admin": "21232f297a57a5a743894a0e4a801fc3"   # Password: admin (MD5 - insecure hashing)
}

BALANCES = {
    "user1": 1000,
    "admin": 5000
}

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def authenticate(username, password):
    if username in USERS and USERS[username] == hash_password(password):
        return True
    return False

def get_balance(username):
    if username in BALANCES:
        return BALANCES[username]
    return 0

def deposit(username, amount):
    if amount <= 0:
        print("Invalid deposit amount!")
        return
    BALANCES[username] += amount
    print(f"Deposited {amount}. New balance: {BALANCES[username]}")

def withdraw(username, amount):
    if amount <= 0:
        print("Invalid withdrawal amount!")
        return
    if amount > BALANCES[username]:
        print("Insufficient funds!")
        return
    BALANCES[username] -= amount
    print(f"Withdrew {amount}. New balance: {BALANCES[username]}")

# Duplicate function (Code duplication issue)
def withdraw_amount(username, amount):
    if amount <= 0:
        print("Invalid withdrawal amount!")
        return
    if amount > BALANCES[username]:
        print("Insufficient funds!")
        return
    BALANCES[username] -= amount
    print(f"Withdrew {amount}. New balance: {BALANCES[username]}")

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if not authenticate(username, password):
        print("Authentication failed!")
        return
    
    print("Login successful!")
    print("1. Check Balance\n2. Deposit\n3. Withdraw")
    choice = input("Enter choice: ")
    
    if choice == "1":
        print(f"Your balance: {get_balance(username)}")
    elif choice == "2":
        amount = int(input("Enter deposit amount: "))
        deposit(username, amount)
    elif choice == "3":
        amount = int(input("Enter withdrawal amount: "))
        withdraw(username, amount)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
