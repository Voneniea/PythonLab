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


arr = [3, 1, 4, 1, 5, 9, 2]
print(f"Массив: {arr}")
choice = input(
    "Выберите функцию: 1 - Проверить глобальный минимум, 2 - Поменять местами минимум и максимум, 3 - Проверить наличие максимального элемента в интервале: ")

if choice == "1":
    index = int(input("Введите индекс: "))
    if is_global_minimum(arr, index):
        print(f"Элемент {arr[index]} по индексу {index} является глобальным минимумом.")
    else:
        print(f"Элемент {arr[index]} по индексу {index} не является глобальным минимумом.")
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
else:
    print("Некорректный выбор.")