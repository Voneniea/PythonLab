def main():
    print("Введите строки (пустая строка для завершения ввода):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    sorted_lines = sorted(lines, key=lambda s: len(s.split()))

    print("\nСтроки, отсортированные по количеству слов:")
    for line in sorted_lines:
        print(line)

if __name__ == "__main__":
    main()
