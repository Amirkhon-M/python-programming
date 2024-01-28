"""
Build a program for calculating the
area of various geometric shapes (circle, rectangle, triangle, etc.)
using separate functions for each shape.
"""


def menu():
    print("1. Rectangle\n2. Square\n3. Circle")
    option = int(input("Option: "))

    if option == 1:
        area = rectangle()
    elif option == 2:
        area = square()
    elif option == 3:
        area = circle()
    else:
        print("Invalid option")
    print(f"The area is: {area}")


def rectangle():
    h = float(input("Enter height: "))
    w = float(input("Enter width: "))
    area = h * w
    return area


def square():
    side = float(input("Enter the side length: "))
    area = side * side
    return area


def circle():
    radius = float(input("Enter the radius: "))
    pi = 3.14
    area = pi * radius**2
    return area


def main():
    menu()


if __name__ == "__main__":
    main()
