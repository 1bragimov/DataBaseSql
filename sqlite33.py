import sqlite3

conn = sqlite3.connect("database.db")

conn.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userid INTEGER NOT NULL,
    fullname VARCHAR(255),
    email VARCHAR(50) UNIQUE 

)''')

# try:
#     conn.execute(''' INSERT INTO users (userid, fullname, email) VALUES (12435,"MsAlice","ms@example.com")
#     ''')
#     print("User added successfully")
# except:
#     print("Database Error code!")

data = conn.execute("SELECT * FROM users")

for x in data:
    print(x)

conn.commit()
conn.close()
