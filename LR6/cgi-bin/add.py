#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import sqlite3
import cgi
import os

form = cgi.FieldStorage()
table = form.getvalue('table')

# Русские названия таблиц и полей
table_names = {
    'employees': 'Сотрудники',
    'positions': 'Должности',
    'applications': 'Заявки'
}

field_names = {
    'employees': {
        'name': 'ФИО',
        'age': 'Возраст',
        'experience': 'Стаж (лет)',
        'position_id': 'ID должности'
    },
    'positions': {
        'title': 'Название',
        'salary': 'Зарплата',
        'requirements': 'Требования'
    },
    'applications': {
        'company_name': 'Компания',
        'position_title': 'Должность',
        'requirements': 'Требования',
        'status': 'Статус'
    }
}

print('''Content-type: text/html; charset=utf-8\n\n
<!DOCTYPE html>
<html>
<head>
    <title>Добавление записи</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>
    <h1>Добавление записи: {}</h1>
    <a href="index.py">На главную</a>
    <form method="post" action="save.py">
        <input type="hidden" name="table" value="{}">
'''.format(table_names.get(table, table), table))

conn = None
try:
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'employment_agency.db'))
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(f"PRAGMA table_info({table})")
    columns = [column[1] for column in cursor.fetchall() if column[1].lower() != 'id']

    for column in columns:
        field_name = field_names.get(table, {}).get(column, column)
        print(f'''
        <div>
            <label>{field_name}:</label><br>
            <input type="text" name="{column}" required>
        </div>
        ''')

    print('''
        <input type="submit" value="Сохранить">
    </form>
    </body>
    </html>
    ''')

except Exception as e:
    print(f'<p>Ошибка: {str(e)}</p>')
finally:
    if conn:
        conn.close()