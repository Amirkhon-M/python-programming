"""
Get two numbers from the user using input prompt.
If A is greater than B return A is greater than b, if A is less b return B is smaller than B, else A is equal to B
"""


def compare(a: int, b: int):
    if a > b:
        result = a - b
        result = "The first number is greater than the second one for: " + str(result)
    elif a < b:
        result = b - a
        result = "The second number is greater than the first one for: " + str(result)
    else:
        return "Both numbers are equal!"
    return display_result(result)


def main():
    test()
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return compare(a, b)
    return compare_for_test(a, b)


def display_result(result):
    print(result)


def test():
    a, b = 4, 3
    expected_output = "The first number is greater than the second one for: 1"
    actual_output = compare_for_test(a, b)
    assert actual_output == expected_output, "Results not matching."


def compare_for_test(a: int, b: int):
    if a > b:
        result = a - b
        result = "The first number is greater than the second one for: " + str(result)
    elif a < b:
        result = b - a
        result = "The second number is greater than the first one for: " + str(result)
    else:
        return "Both numbers are equal!"
    return result


def run_tests():
    test()


if __name__ == "__main__":
    run_tests()
    main()
