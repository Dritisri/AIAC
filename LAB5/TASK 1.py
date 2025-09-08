import hashlib
import getpass
import json
import os

USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    users = load_users()
    username = input("Enter new username: ")
    if username in users:
        print("Username already exists.")
        return
    password = getpass.getpass("Enter new password: ")
    users[username] = hash_password(password)
    save_users(users)
    print("Registration successful.")

def login():
    users = load_users()
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    if username in users and users[username] == hash_password(password):
        print("Login successful.")
    else:
        print("Invalid username or password.")

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()