import math


def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


def product_of_digits(n):
    product = 1
    for digit in str(n):
        if digit != '0':
            product *= int(digit)
    return product


def is_coprime(a, b):
    return math.gcd(a, b) == 1


def sum_divisors_condition(n):
    sum_d = sum_of_digits(n)
    prod_d = product_of_digits(n)
    total = 0

    for i in range(1, n + 1):
        if n % i == 0 and is_coprime(i, sum_d) and not is_coprime(i, prod_d):
            total += i

    return total


num = int(input("Введите число: "))
result = sum_divisors_condition(num)
print(f"Сумма делителей числа {num}, взаимно простых с суммой цифр и не взаимно простых с произведением цифр: {result}")
