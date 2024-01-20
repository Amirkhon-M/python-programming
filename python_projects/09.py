from colorama import Fore
import time


def square():
    print(Fore.LIGHTBLUE_EX + "1. Find Area")
    print("2. Find Perimeter")
    option = int(input(Fore.MAGENTA + "Option: "))
    if option == 1:
        side = float(input(Fore.LIGHTBLUE_EX + "Enter side: "))
        result = side * side
    elif option == 2:
        side = float(input(Fore.LIGHTBLUE_EX + "Enter side: "))
        result = side * 4
    else:
        print("Invalid input")
        return

    print(Fore.LIGHTGREEN_EX + str(result))


def rectangle():
    print(Fore.LIGHTBLUE_EX + "1. Find Area")
    print("2. Find Perimeter")
    option = int(input(Fore.MAGENTA + "Option: "))
    if option == 1:
        side1 = float(input(Fore.LIGHTBLUE_EX + "Enter length: "))
        side2 = float(input(Fore.LIGHTBLUE_EX + "Enter width: "))
        result = side1 * side2
    elif option == 2:
        side1 = float(input(Fore.LIGHTBLUE_EX + "Enter length: "))
        side2 = float(input(Fore.LIGHTBLUE_EX + "Enter width: "))
        result = (side1 + side2) * 2
    else:
        print("Invalid input")
        return

    print(Fore.LIGHTGREEN_EX + str(result))


def main():
    print(Fore.CYAN + "\n\tMain Menu")
    print(Fore.LIGHTWHITE_EX + "1. Square\n2. Rectangle\n3. Exit")
    option = int(input(Fore.MAGENTA + "Option: "))
    if option == 1:
        square()
    elif option == 2:
        rectangle()
    elif option == 3:
        print("Exiting the program...")
        time.sleep(2)
        exit()
    else:
        print("Invalid input!")


if __name__ == "__main__":
    while True:
        main()
