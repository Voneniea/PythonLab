def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 3 != 0:
            count += 1
    return count

num = int(input("Введите число: "))
result = count_divisors(num)
print(f"Количество делителей числа {num}, не делящихся на 3: {result}")
