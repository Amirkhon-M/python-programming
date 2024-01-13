"""
Problem: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Reference:
    https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%204.md#question-14
"""


def counter(text: str) -> dict:
    """
    The function counts t+he number of lower case and upper case letters in given string.
    """

    num = {"upper_case": 0, "lower_case": 0}

    for i in text:
        if i.isupper():
            num["upper_case"] += 1
        elif i.islower():
            num["lower_case"] += 1
        else:
            continue

    return num


def test_upper_case_count():
    input_data = "HELLO"
    expected_output = {
        "upper_case": 5,
        "lower_case": 0,
    }
    actual_output = counter(input_data)
    assert expected_output == actual_output, "Results not matching."


def test_lower_case_count():
    input_data = "hello"
    expected_output = {
        "upper_case": 0,
        "lower_case": 5,
    }
    actual_output = counter(input_data)
    assert expected_output == actual_output, "Results not matching."


def test_upper_case_and_lower_case_count():
    input_data = "helloHELLO"
    expected_output = {
        "upper_case": 5,
        "lower_case": 5,
    }
    actual_output = counter(input_data)
    assert expected_output == actual_output, "Results not matching."


def run_tests():
    test_upper_case_count()
    test_lower_case_count()
    test_upper_case_and_lower_case_count()


def main():
    # Manual execution.
    text = input("Enter a text to count no. of upper case and lower case letters: ")
    result = counter(text)
    print("UPPER CASE:", result["upper_case"])
    print("LOWER CASE:", result["lower_case"])


if __name__ == "__main__":
    run_tests()
    main()
