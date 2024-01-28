"""
Сумма чисел: Напишите программу, которая запрашивает у
пользователя целое число n и затем вычисляет сумму всех целых
чисел от 1 до n , используя цикл for или while . Посчитайте сумму всех
четных и нечетных чисел тоже
"""


def calc(n: int):
    sum_all = 0
    sum_even = 0
    sum_odd = 0

    for i in range(1, n + 1):
        sum_all += i
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i

    print("Сумма всех чисел от 1 до", n, ":", sum_all)
    print("Сумма четных чисел от 1 до", n, ":", sum_even)
    print("Сумма нечетных чисел от 1 до", n, ":", sum_odd)


def main():
    n = input("Введите целое число: ")

    if n.isdigit():
        n = int(n)
        calc(n)
    else:
        print("Вы ввели не целое число!")


if __name__ == "__main__":
    main()
