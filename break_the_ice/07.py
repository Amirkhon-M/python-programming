"""
Problem:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th
row and j-th column of the array should be i _ j.*
"""


def array(x, y):
    array = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(i * j)
        array.append(row)
    return array


def test():
    expected_output = []
    actual_output = array(0, 0)
    assert expected_output == actual_output, "Results not matching."


def run_test():
    test()
    print("Test passed successfully!")


def main():
    run_test()
    x = int(input("Enter the number of rows (X): "))
    y = int(input("Enter the number of columns (Y): "))
    result_array = array(x, y)
    print("Generated 2D Array:")
    for row in result_array:
        print(row)


if __name__ == "__main__":
    main()
