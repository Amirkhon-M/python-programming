"""
Iterate 0 to 10 using for loop, do the same using while loop.
"""


def for_loop(i: int):
    print("for loop: \n")
    for i in range(11):
        print(i)


def while_loop(i: int):
    print("while loop: \n")
    while i <= 10:
        print(i)
        i += 1


def main():
    i = 0
    for_loop(i)
    while_loop(i)
    return i


if __name__ == "__main__":
    main()
