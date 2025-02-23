operation_map = {
    "write": "w",
    "read": "r",
    "execute": "x"
}

N = int(input("Введите количество файлов: "))

file_permissions = {}

print("Введите имена файлов и допустимые операции:")
for _ in range(N):
    data = input().split()
    file_name = data[0]
    permissions = set(data[1:])
    file_permissions[file_name] = permissions

M = int(input("Введите количество запросов: "))

print("\nРезультаты запросов:")
for _ in range(M):
    operation, file_name = input().split()
    if operation_map[operation] in file_permissions.get(file_name, set()):
        print("OK")
    else:
        print("Access denied")
