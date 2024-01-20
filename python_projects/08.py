"""
Iterate 0 to 10 using for loop, do the same using while loop.
"""


def for_loop():
    print("for loop: \n")
    for i in range(10, -1, -1):
        print(i)


def while_loop():
    print("while loop: \n")
    i = 10
    while i >= 0:
        print(i)
        i -= 1


def main():
    for_loop()
    while_loop()


if __name__ == "__main__":
    main()
