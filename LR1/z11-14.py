def avg_ascii(s: str) -> float:
    if not s:
        return 0
    return sum(ord(ch) for ch in s) / len(s)


def median_ascii(s: str) -> float:
    if not s:
        return 0
    codes = sorted(ord(ch) for ch in s)
    n = len(codes)
    return codes[n // 2]


def max_triple_avg(s: str) -> float:
    n = len(s)
    if n < 3:
        return avg_ascii(s)
    triple_avgs = []
    for i in range(n - 2):
        triple = s[i:i + 3]
        triple_avg = sum(ord(ch) for ch in triple) / 3
        triple_avgs.append(triple_avg)
    return max(triple_avgs)

# Задача 2
def sort_by_avg_ascii(strings: list) -> list:
    return sorted(strings, key=avg_ascii)

# Задача 6
def sort_by_median_ascii(strings: list) -> list:
    return sorted(strings, key=median_ascii)

# Задача 8
def sort_by_quad_deviation(strings: list) -> list:
    return sorted(strings, key=lambda s: abs(max_triple_avg(s) - avg_ascii(s)))

# Задача 11
def sort_by_quad_deviation_from_first(strings: list) -> list:
    if not strings:
        return []
    first_value = max_triple_avg(strings[0])
    return sorted(strings, key=lambda s: (max_triple_avg(s) - first_value) ** 2)


def read_strings_from_keyboard() -> list:
    print("Введите строки (для завершения ввода нажмите Enter на пустой строке):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return lines


def main():
    menu = (
        "Выберите задачу для выполнения:\n"
        "1. В порядке увеличения среднего веса ASCII-кода символов строки.\n"
        "2. В порядке увеличения медианного значения ASCII-кодов символов строки.\n"
        "3. В порядке увеличения квадратичного отклонения между средним ASCII-кодом и\n"
        "   максимальным средним ASCII-кода тройки подряд символов в строке.\n"
        "4. В порядке квадратичного отклонения (квадрат разности) максимального\n"
        "   среднего ASCII-кода тройки символов строки от максимального среднего\n"
        "   ASCII-кода тройки символов в первой строке.\n"
    )
    print(menu)
    choice = input("Введите номер задачи (1, 2, 3 или 4): ").strip()

    strings = read_strings_from_keyboard()

    if not strings:
        print("Список строк пуст!")
        return

    if choice == '1':
        print("\nСтроки, отсортированные по среднему весу ASCII-кодов символов:")
        sorted_strings = sort_by_avg_ascii(strings)
    elif choice == '2':
        print("\nСтроки, отсортированные по медианному значению ASCII-кодов символов:")
        sorted_strings = sort_by_median_ascii(strings)
    elif choice == '3':
        print("\nСтроки, отсортированные по квадратичному отклонению между средним ASCII-кодом\n"
              "и максимальным средним ASCII-кода тройки подряд символов:")
        sorted_strings = sort_by_quad_deviation(strings)
    elif choice == '4':
        print("\nСтроки, отсортированные по квадратичному отклонению (квадрат разности) максимального\n"
              "среднего ASCII-кода тройки символов строки от такового в первой строке:")
        sorted_strings = sort_by_quad_deviation_from_first(strings)
    else:
        print("Неверный выбор!")
        return

    print("\nРезультат сортировки:")
    for s in sorted_strings:
        print(s)


if __name__ == "__main__":
    main()
