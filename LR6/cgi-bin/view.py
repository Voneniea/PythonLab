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

# Словари перевода
table_names = {
    'employees': 'Сотрудники',
    'positions': 'Должности',
    'applications': 'Заявки'
}

field_names = {
    'employees': {
        'id': 'ID',
        'name': 'ФИО',
        'age': 'Возраст',
        'experience': 'Стаж',
        'position_id': 'ID должности'
    },
    'positions': {
        'id': 'ID',
        'title': 'Название',
        'salary': 'Зарплата',
        'requirements': 'Требования'
    },
    'applications': {
        'id': 'ID',
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
    <title>{}</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <script>
        function confirmDelete() {{
            return confirm("Вы точно хотите удалить эту запись?");
        }}
    </script>
</head>
<body>
    <h1>Таблица: {}</h1>
    <div style="margin-bottom: 20px;">
        <a href="index.py">На главную</a>
        <a href="add.py?table={}" style="margin-left: 15px;">Добавить запись</a>
        <a href="export.py?table={}" style="margin-left: 15px;">Экспорт в XML</a>
    </div>
'''.format(table_names.get(table, table),
           table_names.get(table, table),
           table, table))

conn = None
try:
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'employment_agency.db'))
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,))
    if not cursor.fetchone():
        print(f'<p>Таблица "{table}" не существует</p>')
    else:
        cursor.execute(f"PRAGMA table_info({table})")
        columns = [column[1] for column in cursor.fetchall()]

        if not columns:
            print(f'<p>Таблица "{table}" не содержит столбцов</p>')
        else:
            print('<table border="1" style="width:100%; border-collapse: collapse;">')
            print('<thead><tr>')
            for col in columns:
                translated = field_names.get(table, {}).get(col, col)
                print(f'<th style="padding: 8px; border: 1px solid #ddd;">{translated}</th>')
            print('<th style="padding: 8px; border: 1px solid #ddd;">Действия</th>')
            print('</tr></thead>')

            print('<tbody>')
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()

            if not rows:
                print(f'<tr><td colspan="{len(columns) + 1}" style="text-align: center;">Нет данных</td></tr>')
            else:
                for row in rows:
                    print('<tr>')
                    for value in row:
                        print(
                            f'<td style="padding: 8px; border: 1px solid #ddd;">{value if value is not None else "-"}</td>')
                    print(f'''<td style="padding: 8px; border: 1px solid #ddd; text-align: center;">
                        <a href="edit.py?table={table}&id={row[0]}" style="margin-right: 10px;">Редактировать</a>
                        <a href="delete.py?table={table}&id={row[0]}" onclick="return confirmDelete()">Удалить</a>
                    </td>''')
                    print('</tr>')
            print('</tbody></table>')

except Exception as e:
    print(f'<p style="color: red;">Ошибка: {str(e)}</p>')
finally:
    if conn:
        conn.close()

print('''
</body>
</html>
''')