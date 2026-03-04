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
users = cursor.fetchall()

users_list = []
for user in users:
    user_dict = {
        'id': user[0],
        'username': user[1],
        'email': user[2],
        'age': user[3]
    }
    users_list.append(user_dict)

for user in users_list:
    print(user)

connection.commit()
connection.close()
