import random


# Задача 5
def shuffle_string(input_str):
    input_list = list(input_str)
    random.shuffle(input_list)
    return ''.join(input_list)


# Задача 7
def is_palindrome(input_str):
    return input_str == input_str[::-1]

# Задача 14
def sort_words_by_length(input_str):
    words = input_str.split()
    sorted_words = sorted(words, key=len)
    return ' '.join(sorted_words)


def main():
    print("Выберите задачу для выполнения:")
    print("1. Перемешать все символы строки в случайном порядке")
    print("2. Проверить, образуют ли прописные символы палиндром")
    print("3. Упорядочить слова по количеству букв в каждом слове")

    choice = input("Введите номер задачи (1, 2 или 3): ")

    if choice == '1':
        input_str = input("Введите строку для перемешивания: ")
        result = shuffle_string(input_str)
        print(f"Результат: {result}")

    elif choice == '2':
        input_str = input("Введите строку для проверки на палиндром: ")
        result = is_palindrome(input_str)
        if result:
            print("Прописные символы строки образуют палиндром.")
        else:
            print("Прописные символы строки не образуют палиндром.")

    elif choice == '3':
        input_str = input("Введите строку для упорядочивания слов: ")
        result = sort_words_by_length(input_str)
        print(f"Результат: {result}")

    else:
        print("Неверный выбор! Пожалуйста, выберите 1, 2 или 3.")


if __name__ == "__main__":
    main()
