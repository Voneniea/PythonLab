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
record_id = form.getvalue('id')

print('''Content-type: text/html; charset=utf-8\n\n
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="3;url=view.py?table={}">
    <title>Обновление данных</title>
</head>
<body>
'''.format(table))

conn = None
try:
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'employment_agency.db'))
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(f"PRAGMA table_info({table})")
    columns = [column[1] for column in cursor.fetchall() if column[1].lower() != 'id']

    set_clause = ', '.join([f"{col}=?" for col in columns])
    values = [form.getvalue(col) for col in columns]
    values.append(record_id)

    query = f"UPDATE {table} SET {set_clause} WHERE id=?"
    cursor.execute(query, values)
    conn.commit()

    print(f'''
    <h1>Данные успешно обновлены!</h1>
    <p>Вы будете перенаправлены обратно через 3 секунды...</p>
    <p><a href="view.py?table={table}">Вернуться сейчас</a></p>
    ''')

except Exception as e:
    print(f'''
    <h1>Ошибка при обновлении</h1>
    <p>{str(e)}</p>
    <p><a href="javascript:history.back()">Вернуться назад</a></p>
    ''')
finally:
    if conn:
        conn.close()

print('''
</body>
</html>
''')