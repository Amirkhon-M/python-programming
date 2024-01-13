"""
Problem: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
"""


def get_numbers():
    numbers_str = input("Enter comma-separated numbers: ")
    numbers_list = numbers_str.split(",")
    numbers_tuple = tuple(numbers_list)
    return numbers_list, numbers_tuple


def main():
    numbers_list, numbers_tuple = get_numbers()
    print("List:", numbers_list)
    print("Tuple:", numbers_tuple)


if __name__ == "__main__":
    main()
