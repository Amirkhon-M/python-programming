"""
Работа с пользовательским меню: Создайте текстовое меню,
которое предоставляет пользователю несколько опций (например, "1.
Выполнить действие 1", "2. Выполнить действие 2" и так далее).
Control Flow 10
Используйте цикл while , чтобы программа продолжала выполнение,
пока пользователь не выберет опцию выхода. system("exit");

"""


def add_one():
    return 1 + 1


def add_two():
    return 2 + 2


def main():
    answer = 0
    answer0 = 0

    while True:
        print("\nМеню:")
        print("Действие 1: 1 + 1")
        print("Действие 2: 2 + 2")
        print("Действие 3: Выход")

        option = int(input("Выберите действие (1, 2, 3): "))

        if option == 1:
            answer = add_one()
            print(f"Ответ: {answer}")
        elif option == 2:
            answer0 = add_two()
            print(f"Ответ: {answer0}")
        elif option == 3:
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите 1, 2 или 3.")


if __name__ == "__main__":
    main()
