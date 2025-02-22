N = int(input("Введите количество кубиков у Ани: "))
M = int(input("Введите количество кубиков у Бори: "))

anya_colors = set()
print("Введите номера цветов кубиков Ани:")
for _ in range(N):
    anya_colors.add(int(input()))

boris_colors = set()
print("Введите номера цветов кубиков Бори:")
for _ in range(M):
    boris_colors.add(int(input()))

both = sorted(anya_colors & boris_colors)
only_anya = sorted(anya_colors - boris_colors)
only_boris = sorted(boris_colors - anya_colors)

# Выводим результаты в консоль
print("\nРезультаты:")
print(f"{len(both)}", *both)
print(f"{len(only_anya)}", *only_anya)
print(f"{len(only_boris)}", *only_boris)
