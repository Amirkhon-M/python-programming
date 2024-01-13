"""
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive.
 If below 18 give feedback to wait for the missing amount of years.
"""


def check_age(age: int):
    if age < 18 and age <= 0:
        i = 18 - age
        print(
            "You are not old enough to learn to drive! "
            + "Wait "
            + str(i)
            + " more years."
        )
    else:
        print("You are old enough to drive!")


def main():
    age = int(input("Enter your age: "))
    return check_age(age)


if __name__ == "__main__":
    main()
