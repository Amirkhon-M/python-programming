"""
Write a program to swap two values using functions
"""


def swap_values(a, b):
    temp = a
    a = b
    b = temp
    return a, b


def main():
    value1 = 5
    value2 = 10
    print("Before swapping:")
    print("Value 1:", value1)
    print("Value 2:", value2)
    value1, value2 = swap_values(value1, value2)
    print("\nAfter swapping:")
    print("Value 1:", value1)
    print("Value 2:", value2)


if __name__ == "__main__":
    main()
