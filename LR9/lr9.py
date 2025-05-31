import csv
from tkinter import Tk, filedialog
import re


def parse_time(time_str):
    try:
        time_str = time_str.strip()
        if time_str in ('-', ''):
            return float('inf')

        # Нормализуем строку: заменяем "час" на "ч" и убираем лишние пробелы
        time_str = re.sub(r'\s+', ' ', time_str.lower())
        time_str = time_str.replace('час', 'ч').replace('час.', 'ч')

        # Ищем компоненты времени
        hours = mins = secs = 0

        # Обрабатываем часы
        h_match = re.search(r'(\d+)\s*ч', time_str)
        if h_match:
            hours = int(h_match.group(1))

        # Обрабатываем минуты
        m_match = re.search(r'(\d+)\s*мин', time_str)
        if m_match:
            mins = int(m_match.group(1))

        # Обрабатываем секунды
        s_match = re.search(r'(\d+)\s*сек', time_str)
        if s_match:
            secs = int(s_match.group(1))

        return hours * 3600 + mins * 60 + secs
    except:
        return float('inf')


def read_csv(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


def sort_by_time(data):
    return sorted(data, key=lambda x: parse_time(x['Затраченное время']))


def print_results(data):
    for row in data:
        print(f"{row['Фамилия']} {row['Имя']}: {row['Затраченное время']}")


def select_file():
    root = Tk()
    root.withdraw()
    return filedialog.askopenfilename(
        title="Выберите CSV файл",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )


def main():
    try:
        filename = select_file()
        if not filename:
            print("Файл не выбран")
            return

        data = read_csv(filename)
        sorted_data = sort_by_time(data)
        print("\nСписок слушателей в порядке времени выполнения теста (от меньшего к большему):")
        print_results(sorted_data)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()