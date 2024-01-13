"""
Problem:

Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 _ C _ D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.

Reference:

https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%202.md
"""

import math


def calculation(input_sequence):
    C = 50
    H = 30
    result = []

    for d in input_sequence.split(","):
        d = int(d.strip())
        q = math.sqrt((2 * C * d) / H)
        result.append(q)

    return result


def test():
    input_data = "30"
    expected_output = [10.0]
    actual_output = calculation(input_data)
    assert expected_output == actual_output, "Results not matching."


def run_tests():
    test()
    print("Tests passed successfully")


def main():
    run_tests()
    input_sequence = input("Enter comma-separated values for D: ")
    result = calculation(input_sequence)
    print("Resulting values of Q:", result)


if __name__ == "__main__":
    main()
