#Задача 5
def is_global_minimum(arr, index):
    if not (0 <= index < len(arr)):
        raise ValueError("Индекс выходит за пределы массива")

    return arr[index] == min(arr)

#Задача 17
def swap_min_max(arr):
    min_val = min(arr)
    max_val = max(arr)
    min_index = arr.index(min_val)
    max_index = arr.index(max_val)
    arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
    return arr

#Задача 29
def is_max_in_interval(arr, a, b):
    if not (0 <= a <= b < len(arr)):
        raise ValueError("Некорректный интервал")

    max_val = max(arr)
    return any(arr[i] == max_val for i in range(a, b + 1))

#Задача 41
def average_absolute_value(arr):
    return sum(abs(x) for x in arr) / len(arr)


#Задача 53
def filter_elements_between_avg_and_max(arr):
    avg = sum(arr) / len(arr)
    max_val = max(arr)
    return [x for x in arr if avg < x < max_val]


arr = [3, 1, 4, 1, 5, 9, 2]
print(f"Массив: {arr}")
choice = input(
    "Выберите функцию:\n"
    "1 - Проверить  минимум\n"
    "2 - Поменять местами минимум и максимум\n"
    "3 - Проверить наличие максимального элемента в интервале\n"
    "4 - Найти среднее арифметическое модулей элементов\n"
    "5 - Построить новый список с элементами, большими, чем среднее арифметическое, но меньшими, чем максимальное значение\n"
)

if choice == "1":
    index = int(input("Введите индекс: "))
    if is_global_minimum(arr, index):
        print(f"Элемент {arr[index]} по индексу {index} является минимумом.")
    else:
        print(f"Элемент {arr[index]} по индексу {index} не является минимумом.")
elif choice == "2":
    arr = swap_min_max(arr)
    print(f"Обновленный массив: {arr}")
elif choice == "3":
    a = int(input("Введите начало интервала: "))
    b = int(input("Введите конец интервала: "))
    if is_max_in_interval(arr, a, b):
        print(f"Максимальный элемент массива присутствует в интервале {a}..{b}.")
    else:
        print(f"Максимального элемента массива нет в интервале {a}..{b}.")
elif choice == "4":
    avg_abs = average_absolute_value(arr)
    print(f"Среднее арифметическое модулей элементов массива: {avg_abs}")
elif choice == "5":
    new_arr = filter_elements_between_avg_and_max(arr)
    print(f"Новый список: {new_arr}")
else:
    print("Некорректный выбор.")