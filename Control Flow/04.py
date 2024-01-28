"""
 Игра "Угадай число": Создайте простую игру, в которой программа
загадывает число ( int number = 42; ) а пользователь должен угадать это
число, получая подсказки (больше или меньше). Используйте цикл
while для обработки игрового процесса. Если пользователь находит
число, остановите программу и выведите количество попыток
предпринятых пользователем
"""

import random


def guess_the_number():
    number_to_guess = random.randint(1, 50)
    attempts = 0

    print("Давайте начнем игру! Я загадал число от 1 до 50.")

    while True:
        user_guess = input("Введите вашу догадку: ")

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

        attempts += 1

        if user_guess == number_to_guess:
            print(
                f"Поздравляем! Вы угадали число {number_to_guess} за {attempts} попыток."
            )
            break
        elif user_guess < number_to_guess:
            print("Загаданное число больше. Попробуйте еще раз.")
        else:
            print("Загаданное число меньше. Попробуйте еще раз.")


if __name__ == "__main__":
    guess_the_number()
