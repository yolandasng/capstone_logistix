# check_db.py
import sqlite3

def check_users():
    conn = sqlite3.connect("data/users.db")
    c = conn.cursor()
    
    # Cek tabel users
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    
    print("Daftar User:")
    for row in rows:
        print(row)
    
    conn.close()

if __name__ == "__main__":
    check_users()