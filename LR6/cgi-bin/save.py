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

print('''Content-type: text/html; charset=utf-8\n\n
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="3;url=view.py?table={}">
    <title>Сохранение данных</title>
</head>
<body>
'''.format(table))

try:
    conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'employment_agency.db')))
    cursor = conn.cursor()

    cursor.execute(f"PRAGMA table_info({table})")
    columns = [column[1] for column in cursor.fetchall() if column[1].lower() != 'id']
    values = [form.getvalue(col) for col in columns]

    query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['?']*len(columns))})"
    cursor.execute(query, values)
    conn.commit()

    print(f'''
    <h1>Данные успешно сохранены!</h1>
    <p>Вы будете перенаправлены обратно через 3 секунды...</p>
    <p><a href="view.py?table={table}">Вернуться сейчас</a></p>
    ''')

except Exception as e:
    print(f'''
    <h1>Ошибка при сохранении</h1>
    <p>{str(e)}</p>
    <p><a href="javascript:history.back()">Вернуться назад</a></p>
    ''')
finally:
    if 'conn' in locals():
        conn.close()

print('''
</body>
</html>
''')