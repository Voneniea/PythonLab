def find_min_odd_digit(n):
    min_odd = float('inf')
    for digit in str(n):
        if int(digit) % 2 == 1:
            min_odd = min(min_odd, int(digit))
    return min_odd if min_odd != float('inf') else None

num = int(input("Введите число: "))
result = find_min_odd_digit(num)
if result is not None:
    print(f"Минимальная нечетная цифра числа {num}: {result}")
else:
    print(f"В числе {num} нет нечетных цифр.")
