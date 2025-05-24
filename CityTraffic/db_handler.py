import sqlite3
import bcrypt

def connect_db():
    """Connect to the SQLite database."""
    conn = sqlite3.connect('users.db')
    return conn

def create_table():
    """Create the users table if it doesn't exist."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit() # this saves the changes to the database 
    conn.close()

def insert_user(username, hashed_password):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        # This error occurs if the username already exists
        conn.close()
        return False


def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def verify_password(stored_hash, provided_password):
    if isinstance(stored_hash, str):
        stored_hash = stored_hash.encode('utf-8')
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_hash)
