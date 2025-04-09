import sqlite3

# Подключение к БД (файл создастся автоматически)
conn = sqlite3.connect('employment_agency.db')
cursor = conn.cursor()

# 1. Таблица "Должности" (positions)
cursor.execute('''
CREATE TABLE IF NOT EXISTS positions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    salary REAL,
    requirements TEXT
)
''')

# 2. Таблица "Сотрудники" (employees)
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    experience INTEGER,
    position_id INTEGER,
    FOREIGN KEY (position_id) REFERENCES positions (id)
)
''')

# 3. Таблица "Заявки" (applications)
cursor.execute('''
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    position_title TEXT NOT NULL,
    requirements TEXT,
    status TEXT DEFAULT 'open'
)
''')

# Заполняем таблицы тестовыми данными
# 1. Добавляем должности
cursor.executemany(
    'INSERT INTO positions (title, salary, requirements) VALUES (?, ?, ?)',
    [
        ('Менеджер по продажам', 50000, 'Опыт работы от 1 года'),
        ('Программист Python', 120000, 'Знание Django, Flask'),
        ('Бухгалтер', 70000, 'Высшее экономическое образование')
    ]
)

# 2. Добавляем сотрудников
cursor.executemany(
    'INSERT INTO employees (name, age, experience, position_id) VALUES (?, ?, ?, ?)',
    [
        ('Иванов Иван', 30, 5, 1),  # position_id=1 (Менеджер)
        ('Петрова Мария', 25, 2, 2),  # position_id=2 (Программист)
        ('Сидоров Алексей', 40, 15, 3)  # position_id=3 (Бухгалтер)
    ]
)

# 3. Добавляем заявки
cursor.executemany(
    'INSERT INTO applications (company_name, position_title, requirements) VALUES (?, ?, ?)',
    [
        ('ООО "Технологии"', 'Программист Python', 'Опыт работы от 3 лет'),
        ('АО "Финансы"', 'Бухгалтер', 'Знание 1С'),
        ('ИП "Сервис"', 'Менеджер по продажам', 'Коммуникабельность')
    ]
)

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print("База данных создана и заполнена тестовыми данными!")