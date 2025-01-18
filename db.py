import sqlite3

class DateBase():
    def __init__(self):

        # Устанавливаем соединение с базой данных
        self.con = sqlite3.connect('database.db')
        self.cursor = cursor = self.con.cursor()

        # Создаем таблицу Product
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Product (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        link TEXT NOT NULL,
        image TEXT NOT NULL
        )
        ''')

        # Сохраняем изменения
        self.con.commit()

    def get_products(self):
        self.cursor.execute('SELECT * FROM Product')
        return self.cursor.fetchall()
    
    def add_product(self, title, description, link, image):
        # Добавляем нового пользователя
        self.cursor.execute('INSERT INTO Product (title, description, link, image) VALUES (?, ?, ?, ?)', (title, description, link, image))
        # Сохраняем изменения 
        self.con.commit()