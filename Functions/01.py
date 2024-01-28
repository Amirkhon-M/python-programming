"""
Write a program to calculate area of a circle using functions.
"""


def calculate_area(r: float):
    pi = 3.14
    return pi * r * r


def main():
    print("Enter the radius of circle to find area")
    r = float(input("Radius: "))
    result = calculate_area(r)
    print("Answer: " + str(result))
    return r


if __name__ == "__main__":
    main()
