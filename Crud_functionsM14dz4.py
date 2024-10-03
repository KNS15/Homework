import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    ''')

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INT PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL)
    """)

    for i in range(1, 6):
        cursor.execute("""
        INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)
        """, (f'{i}', f'Product {i}', f'Description {i}', f'Price{i * 61.4}'))

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    all_products = cursor.fetchall()
    connection.commit()
    connection.close()
    return all_products


def add_user(username, email, age):
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)""", (username, email, age, 1000))
    connection.commit()
    connection.close()


def is_included(username):
    return bool(cursor.execute('SELECT COUNT(*) FROM Users WHERE username = ?', (username, )
        ).fetchone()[0])


if __name__ == '__main__':
    initiate_db()