import sqlite3
from typing import Literal

def authenticate(username: str, password: str) -> Literal["empty", "invalid", "success"]:
    """Authenticate user credentials.
    
    Returns:
        "empty" if username/password is empty
        "invalid" if credentials are wrong
        "success" if authentication succeeds
    """
    if not username.strip() or not password.strip():
        return "empty"
    
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?", 
        (username.strip(), password.strip())
    )
    result = c.fetchone()
    conn.close()

    return "success" if result else "invalid"
