def find_max_sum(file_name):
    with open(file_name, 'r') as f:
        n, k = map(int, f.readline().split())
        a = [int(x) for x in f]

    one = 0
    two = 0
    three = 0

    for i in range(2 * k, n):
        one = max(one, a[i - 2 * k])
        two = max(two, one + a[i - k])
        three = max(three, two + a[i])

    return three

result_a = find_max_sum("27-166a.txt")
result_b = find_max_sum("27-166b.txt")

print("Результат для файла A:", result_a)
print("Результат для файла B:", result_b)