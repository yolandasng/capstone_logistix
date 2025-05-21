import sqlite3

def init_db():
    """Initialize the database with required tables."""
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    
    # Create users table if not exists
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            full_name TEXT,
            role TEXT DEFAULT 'user'
        )
    """)
    
    # Add default admin user if not exists
    c.execute("SELECT * FROM users WHERE username = ?", ("admin",))
    if not c.fetchone():
        c.execute(
            "INSERT INTO users (username, password, full_name, role) VALUES (?, ?, ?, ?)", 
            ("admin", "123456", "Administrator", "admin")
        )
    
    conn.commit()
    conn.close()

def add_user(username: str, password: str, full_name: str, role: str = "user"):
    """Add a new user to the database."""
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute(
            "INSERT INTO users (username, password, full_name, role) VALUES (?, ?, ?, ?)",
            (username, password, full_name, role)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    init_db()