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


arr = [3, 1, 4, 1, 5, 9, 2]
print(f"Массив: {arr}")
choice = input("Выберите функцию: 1 - Проверить глобальный минимум, 2 - Поменять местами минимум и максимум: ")

if choice == "1":
    index = int(input("Введите индекс: "))
    if is_global_minimum(arr, index):
        print(f"Элемент {arr[index]} по индексу {index} является глобальным минимумом.")
    else:
        print(f"Элемент {arr[index]} по индексу {index} не является глобальным минимумом.")
elif choice == "2":
    arr = swap_min_max(arr)
    print(f"Обновленный массив: {arr}")
else:
    print("Некорректный выбор.")
