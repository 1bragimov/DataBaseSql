import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userid INTEGER NOT NULL,
    fullname VARCHAR(234) NOT NULL
)''')

conn.commit()


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, userid, fullname):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (userid,fullname) VALUES (?,?)", (userid, fullname))

    def get_all_users(self):
        with self.connection:
            return self.cursor.execute("SELECT userid, fullname FROM users").fetchall()
