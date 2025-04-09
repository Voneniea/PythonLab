import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'employment_agency.db')
conn = sqlite3.connect(db_path)

cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Таблицы в БД:", cursor.fetchall())

cursor.execute("SELECT * FROM employees")
print("Сотрудники:", cursor.fetchall())

conn.close()