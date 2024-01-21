from colorama import Fore
import time


def square(side):
    print(Fore.LIGHTBLUE_EX + "1. Find Area")
    print("2. Find Perimeter")
    option = int(input(Fore.MAGENTA + "Option: "))

    if option == 1:
        result = side * side
    elif option == 2:
        result = side * 4
    else:
        print("Invalid input")
        return

    print(Fore.LIGHTGREEN_EX + str(result))


def rectangle(side1, side2):
    print(Fore.LIGHTBLUE_EX + "1. Find Area")
    print("2. Find Perimeter")

    option = int(input(Fore.MAGENTA + "Option: "))

    if option == 1:
        result = side1 * side2
    elif option == 2:
        result = (side1 + side2) * 2
    else:
        print("Invalid input")
        return

    print(Fore.LIGHTGREEN_EX + str(result))


def get_square_side():
    return float(input(Fore.LIGHTBLUE_EX + "Enter side: "))


def get_rectangle_sides():
    side1 = float(input(Fore.LIGHTBLUE_EX + "Enter length: "))
    side2 = float(input(Fore.LIGHTBLUE_EX + "Enter width: "))
    return rectangle(side1, side2)


def main():
    print(Fore.CYAN + "\n\tMain Menu")
    print(Fore.LIGHTWHITE_EX + "1. Square\n2. Rectangle\n3. Exit")
    option = int(input(Fore.MAGENTA + "Option: "))

    if option == 1:
        square(get_square_side())
    elif option == 2:
        sides = get_rectangle_sides()
        rectangle(*sides)
    elif option == 3:
        print("Exiting the program...")
        time.sleep(2)
        exit()
    else:
        print("Invalid input!")


if __name__ == "__main__":
    while True:
        main()
