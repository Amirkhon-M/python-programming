import os
import time
import qr
from colorama import *



if os.path.exists("db.txt"):
    with open("db.txt", "r") as file:
        pass
else:
    print("Some files may be missing... :(")
    exit()


def main():
    text = ("***Main Menu***\n"
            "1. Convert student's data to QR-code\n"
            "0. Exit\n")
    while True:
        print(Fore.LIGHTWHITE_EX + text)
        option = int(input(Fore.LIGHTGREEN_EX + "Option: "))
        if option == 0:
            exit()
        elif option == 1:
            qr.data()
        else:
            print(Fore.RED + "\nInvalid option!\n")

if __name__ == "__main__":
    main()
