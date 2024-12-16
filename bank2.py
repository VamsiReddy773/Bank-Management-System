import sqlite3
import bcrypt

def initialize_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute
    conn.commit()
    conn.close()


def register_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()
    if result:
        stored_password = result[0]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            print("Login successful!")
        else:
            print("Invalid password.")
    else:
        print("User not found.")

def main():
    initialize_db()
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            login_user(username, password)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
