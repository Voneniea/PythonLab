import re

# Задача 6
def count_numbers_greater_than_five(input_str):
    numbers = re.findall(r'\d+', input_str)
    count = sum(1 for num in numbers if int(num) > 5)
    return count


# Задача 12
def find_unused_cyrillic(input_str):
    cyrillic_alphabet = set("абвгдежзийклмнопрстуфхцчшщъыьэюя")
    input_chars = set(input_str.lower())
    missing_letters = cyrillic_alphabet - input_chars
    return ''.join(sorted(missing_letters))


# Задача 13
def find_max_natural_number(input_str):
    numbers = re.findall(r'\d+', input_str)
    naturals = [int(num) for num in numbers if int(num) > 0]
    return max(naturals) if naturals else None


def main():
    print("Выберите задачу для выполнения:")
    print("1. Подсчитать количество чисел в строке, значение которых больше 5")
    print("2. Найти символы кириллицы, которые не задействованы в строке")
    print("3. Найти максимальное из имеющихся в строке натуральных чисел")

    choice = input("Введите номер задачи (1, 2 или 3): ").strip()

    if choice == '1':
        sample_str = "1 3 5 142 0 2 5 6"
        print("\nИсходная строка:")
        print(sample_str)
        count = count_numbers_greater_than_five(sample_str)
        print(f"\nКоличество чисел больше 5: {count}")

    elif choice == '2':
        sample_str = "Я люблю питон и не люблю математику"
        print("\nИсходная строка:")
        print(sample_str)
        missing = find_unused_cyrillic(sample_str)
        print("\nСимволы кириллицы, отсутствующие в строке:")
        print(missing if missing else "Все буквы использованы")

    elif choice == '3':
        sample_str = "15 8 23 42 9 2"
        print("\nИсходная строка:")
        print(sample_str)
        max_number = find_max_natural_number(sample_str)
        if max_number is not None:
            print(f"\nМаксимальное натуральное число: {max_number}")
        else:
            print("\nВ строке нет натуральных чисел.")

    else:
        print("Неверный выбор! Пожалуйста, выберите 1, 2 или 3.")


if __name__ == "__main__":
    main()
