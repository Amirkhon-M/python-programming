"""
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to
get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger
differences, and a custom text if my_age = your_age
"""


def check_age(age: int):
    my_age = 14
    if my_age < age:
        compare = age - my_age
        print("You are older than me for " + str(compare) + " years")
    elif my_age > age:
        compare = my_age - age
        print("I am older than you for " + str(compare) + " years")
    else:
        print("We are the same age )")


def main():
    age = int(input("Enter your age: "))
    while age < 0:
        age = int(input("Enter valid age: "))
    return check_age(age)


if __name__ == "__main__":
    main()
