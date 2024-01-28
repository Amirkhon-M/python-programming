"""
Simple Calculator Program: Create a program that acts as a basic calculator,
allowing users to perform addition, subtraction, multiplication, and division. Use
functions for each operation.

"""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b != 0:
        return a / b
    else:
        print("Error: Division by zero")
        return None


def main():
    print("Simple Calculator\n")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

    option = int(input("Select operation (1/2/3/4): "))
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if option == 1:
        result = add(num1, num2)
    elif option == 2:
        result = subtract(num1, num2)
    elif option == 3:
        result = multiply(num1, num2)
    elif option == 4:
        result = divide(num1, num2)
    else:
        print("Invalid input. Please enter a valid option.")
        return

    if result is not None:
        print("Result:", result)


if __name__ == "__main__":
    main()
