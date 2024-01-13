"""
Problem:
Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple which contains every number.
"""


def solution(input_data: str) -> tuple:
    numbers_list = input_data.split(",")
    numbers_tuple = tuple(numbers_list)
    return numbers_list, numbers_tuple


def test1():
    input_data = "34,67,55,33,12,98"
    expected_output = (
        ["34", "67", "55", "33", "12", "98"],
        ("34", "67", "55", "33", "12", "98"),
    )
    actual_output = solution(input_data)
    assert expected_output == actual_output, "Results not matching."


def test2():
    input_data = "1,2,3,4,5"
    expected_output = (["1", "2", "3", "4", "5"], ("1", "2", "3", "4", "5"))
    actual_output = solution(input_data)
    assert expected_output == actual_output, "Results not matching."


def run_tests():
    test1()
    test2()


def main():
    input_data = input("Enter a sequence of comma-separated numbers: ")
    result_list, result_tuple = solution(input_data)
    print("List:", result_list)
    print("Tuple:", result_tuple)


if __name__ == "__main__":
    run_tests()
    main()
