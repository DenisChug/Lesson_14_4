import sqlite3

def initiate_db():
    connection = sqlite3.connect('Prod.db')
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS Prod')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Prod
                 (id INTEGER PRIMARY KEY,
                 title TEXT NOT NULL,
                 description TEXT,
                 price INTEGER NOT NULL)
                 ''')

    products = [
        {"name": "Яблоки", "description": "Яблоко как яблоко", "price": 100, },
        {"name": "Груши", "description": "Груша как груша", "price": 200},
        {"name": "Апельсины", "description": "Апельсин как апельсин", "price": 300},
        {"name": "Бананы", "description": "Банан как банан", "price": 400}]

    for product in products:
        cursor.execute('INSERT INTO Prod (title, description, price)VALUES(?, ?, ?)',
                       (f"{product['name']}",f"{product['description']}", f"{product['price']}"))

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('Prod.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Prod")
    products = cursor.fetchall()
    connection.close()
    return products