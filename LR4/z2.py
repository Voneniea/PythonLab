def frequency(file):
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    letter_counts = {}
    for char in text:
        if 'а' <= char <= 'я' or char == 'ё':
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    total = sum(letter_counts.values())

    for letter, x in letter_counts.items():
        percentage = (x / total) * 100
        print(f"{letter}: {percentage:.2f}%")

file = 'z2.txt'
frequency(file)