"""
Problem: With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8
"""


def generate_square_dict(n):
    square_dict = {}
    for i in range(1, n + 1):
        square_dict[i] = i * i
    return square_dict


def solution(n):
    result_dict = generate_square_dict(n)
    return result_dict


def test1():
    input_data = 8
    expected_output = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
    actual_output = solution(input_data)
    assert expected_output == actual_output, "Results not matching."


def test2():
    input_data = 5
    expected_output = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    actual_output = solution(input_data)
    assert expected_output == actual_output, "Results not matching."


def run_tests():
    test1()
    test2()


def main():
    n = int(input("Enter an integral number (n): "))
    result_dict = solution(n)
    print(result_dict)


if __name__ == "__main__":
    run_tests()
    main()
