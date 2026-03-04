import sqlite3


connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER
    )
''')

cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', 
               ('newuser', 'newuser@example.com', 28))
cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', 
               ('user1', 'newuser1@example.com', 25))

cursor.execute('SELECT * FROM Users')
first_user = cursor.fetchone()
print(first_user)

cursor.execute('SELECT * FROM Users')
first_five_users = cursor.fetchmany(5)
print(first_five_users)

cursor.execute('SELECT * FROM Users')
all_users = cursor.fetchall()
print(all_users)

connection.commit()
connection.close()
