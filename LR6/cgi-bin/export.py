#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import sqlite3
import xml.etree.ElementTree as ET
import cgi
import os


def export_table_to_xml(table_name):
    try:
        # Подключение к базе данных
        db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'employment_agency.db'))
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Создаем XML структуру
        root = ET.Element(table_name)

        # Получаем данные из таблицы
        cursor.execute(f"SELECT * FROM {table_name}")
        columns = [column[0] for column in cursor.description]  # Названия столбцов

        for row in cursor.fetchall():
            record = ET.SubElement(root, "record")
            for col_name, value in zip(columns, row):
                field = ET.SubElement(record, col_name)
                field.text = str(value) if value is not None else ""

        # Сохраняем XML файл
        xml_file = f"{table_name}_export.xml"
        full_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', xml_file))

        # Создаем директорию если не существует
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        ET.ElementTree(root).write(full_path, encoding='utf-8', xml_declaration=True)
        return xml_file

    except Exception as e:
        raise Exception(f"Ошибка при экспорте: {str(e)}")
    finally:
        if conn:
            conn.close()


# Основной обработчик CGI
print("Content-type: text/html; charset=utf-8\n\n")
print('''<!DOCTYPE html>
<html>
<head>
    <title>Экспорт данных</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>''')

try:
    form = cgi.FieldStorage()
    table = form.getvalue('table')

    if not table:
        print('<h2>Ошибка: не указана таблица для экспорта</h2>')
    else:
        print(f'<h2>Экспорт таблицы {table}</h2>')

        # Выполняем экспорт
        xml_file = export_table_to_xml(table)

        # Выводим результат
        print(f'''
        <p>Таблица успешно экспортирована в XML.</p>
        <p>Файл: <a href="../{xml_file}" download>{xml_file}</a></p>
        <p><a href="view.py?table={table}">Вернуться к таблице</a></p>
        ''')

except Exception as e:
    print(f'''
    <h2>Ошибка</h2>
    <p>{str(e)}</p>
    <p><a href="javascript:history.back()">Назад</a></p>
    ''')

    # Логируем ошибку для отладки
    with open('export_errors.log', 'a', encoding='utf-8') as f:
        f.write(f"Ошибка при экспорте {table}: {str(e)}\n")

print('''</body></html>''')