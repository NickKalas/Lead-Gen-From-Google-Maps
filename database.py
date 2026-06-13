import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT NOT NULL,
    adress TEXT NOT NULL,
    phone_number INTEGER,
    reviews TEXT NOT NULL,
    average TEXT NOT NULL,
    website TEXT NOT NULL
)
""")

def update_database(name, adress, phone_number, reviews, average, website):
    # 'OR IGNORE' tells SQLite to skip saving quietly if a duplicate 'name' is found
    cursor.execute("""
    INSERT OR IGNORE INTO users (name, adress, phone_number, reviews, average, website)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, adress, phone_number, reviews, average, website))
    
    connection.commit()

# --- Testing / Printing Block ---
# (This part will run if you execute database.py directly to check your current entries)
if __name__ == "__main__":
    cursor.execute("SELECT * FROM users")
    all_users = cursor.fetchall()

    print("All users in the Database: ")
    for user in all_users:
        print(user)
