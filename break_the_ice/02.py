"""
Problem: Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320
"""


def calculate_factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)


def test():
    input_data = 5
    expected_output = 120
    actual_output = calculate_factorial(input_data)
    assert expected_output == actual_output, "Results not matching."


def main():
    number = int(input("Enter a number: "))
    factorial_result = calculate_factorial(number)
    print(f"The factorial of {number}! is: {factorial_result}")


if __name__ == "__main__":
    test()
    main()
