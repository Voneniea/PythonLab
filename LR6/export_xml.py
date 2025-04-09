#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import xml.etree.ElementTree as ET
import os


def export_table_to_xml(table_name):
    # Подключение к БД
    db_path = os.path.abspath('employment_agency.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Создаем корневой элемент XML
    root = ET.Element(table_name)

    # Получаем данные из таблицы
    cursor.execute(f"SELECT * FROM {table_name}")
    columns = [column[0] for column in cursor.description]  # Получаем названия столбцов

    for row in cursor.fetchall():
        record = ET.SubElement(root, "record")
        for col_name, value in zip(columns, row):
            field = ET.SubElement(record, col_name)
            field.text = str(value)

    # Сохраняем в файл
    tree = ET.ElementTree(root)
    xml_file = f"{table_name}_export.xml"
    tree.write(xml_file, encoding='utf-8', xml_declaration=True)

    conn.close()
    return xml_file


# Пример использования
if __name__ == "__main__":
    tables = ['employees', 'positions', 'applications']
    for table in tables:
        xml_file = export_table_to_xml(table)
        print(f"Таблица {table} экспортирована в {xml_file}")