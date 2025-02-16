def is_global_minimum(arr, index):
    if not (0 <= index < len(arr)):
        raise ValueError("Индекс выходит за пределы массива")

    return arr[index] == min(arr)


arr = [3, 1, 4, 1, 5, 9, 2]
print(f"Массив: {arr}")
index = int(input("Введите индекс: "))

if is_global_minimum(arr, index):
    print(f"Элемент {arr[index]} по индексу {index} является глобальным минимумом.")
else:
    print(f"Элемент {arr[index]} по индексу {index} не является глобальным минимумом.")
