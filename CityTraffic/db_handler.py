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
            password TEXT NOT NULL,
            login_time TEXT
        )
    ''')
    conn.commit() # this saves the changes to the database 
    conn.close()

def add_login_time_column():
    conn = connect_db()
    cursor = conn.cursor()

    # Check if the column already exists
    cursor.execute("PRAGMA table_info(users)")
    columns = [col[1] for col in cursor.fetchall()]
    
    if "login_time" not in columns:
        print("[INFO] Adding missing 'login_time' column to users table.")
        cursor.execute("ALTER TABLE users ADD COLUMN login_time TEXT")
        conn.commit()
    else:
        print("[INFO] 'login_time' column already exists.")

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
    
def update_last_login(username, timestamp):
    # SQL update statement to update last_login in DB for this username
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET login_time = ? WHERE username = ?", (timestamp, username))
    conn.commit()
    conn.close()



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


def fetch_logged_in_users():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row  # ✅ THIS LINE converts row results to dict-like objects
    cursor = conn.cursor()

    cursor.execute("SELECT username, login_time FROM users")
    rows = cursor.fetchall()

    users = [dict(row) for row in rows]  # ✅ Convert sqlite3.Row to regular dict
    conn.close()
    return users

'''
cursor is the object that allows us to interact with the database
execute() is used to send the commands to the database
'''
