"""
Problem: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Reference:
    https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%204.md#question-15
"""


def compute_expression(a):
    a1 = int(str(a) * 2)
    a2 = int(str(a) * 3)
    a3 = int(str(a) * 4)
    result = int(a + a1 + a2 + a3)
    return result


def test():
    input_data = 9
    expected_output = 11106
    assert compute_expression(input_data) == expected_output, "Results not matching."


def run_tests():
    test()


def main():
    number = int(input("Enter number: "))
    result = compute_expression(number)
    print(
        f"The result of {number} + {number}{number} + {number}{number}{number} is: {result}"
    )


if __name__ == "__main__":
    run_tests()
    main()
