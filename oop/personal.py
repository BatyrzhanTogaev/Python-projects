import sqlite3


def connect():
    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()
    return conn, cursor


def close(conn):
    conn.commit()
    conn.close()


conn, cursor = connect()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY  AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            salary INTEGER NOT NULL,
            hours INTEGER NOT NULL,
            summa INTEGER NOT NULL
        )
''')

close(conn)


class Person:
    def __init__(self, name, surname, salary, hours):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.hours = hours
        self.summa = salary * hours

    def save(self):
        conn, cursor = connect()

        cursor.execute('''
            INSERT INTO persons (name, surname, salary, hours, summa)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.name, self.surname, self.salary, self.hours, self.summa))

        close(conn)

    def info(self):
        return f'Работник {self.name} {self.surname} зарплата - {self.summa}'


person1 = Person('Батыржан', 'Тогаев', 10000, 60)
person1.save()

person2 = Person('Адиль', 'Ибраев', 8000, 60)
person2.save()
print(person1.info())
