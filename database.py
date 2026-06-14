import sqlite3

DB_FILE = 'database.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        adress TEXT NOT NULL,
        phone_number TEXT,
        reviews TEXT NOT NULL,
        average TEXT NOT NULL,
        website TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

init_db()

def update_database(name, adress, phone_number, reviews, average, website):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT OR IGNORE INTO users (name, adress, phone_number, reviews, average, website)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, adress, phone_number, reviews, average, website))
    
    conn.commit()
    
    conn.close()