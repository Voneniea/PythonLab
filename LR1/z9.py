def main():
    print("Введите строки (пустая строка для завершения ввода):")
    lines = []
    while True:
        s = input()
        if s == "":
            break
        lines.append(s)

    sorted_lines = sorted(lines, key=len)

    print("\nСтроки, отсортированные по длине:")
    for line in sorted_lines:
        print(line)

if __name__ == '__main__':
    main()
