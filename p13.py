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

try:
    cursor.execute('BEGIN')
    
    cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', 
                   ('user1', 'user1@example.com'))
    cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', 
                   ('user2', 'user2@example.com'))
    
    cursor.execute('COMMIT')
    
except:
    cursor.execute('ROLLBACK')
    
connection.commit()
connection.close()
