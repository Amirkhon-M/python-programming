"""
Write a program to convert time to minutes using functions. (input 3 variables
namely hours, minutes and seconds. Convert everything into minutes.)
"""


def hours_to_minutes(hrs: float):
    return hrs * 60


def seconds_to_minutes(secs: float):
    return secs / 60


def main():
    print("This application converts seconds or hours to minutes.")
    print("1. Hours to minutes\n2. Seconds to minutes")

    option = int(input("Option: "))

    if option == 1:
        hrs = float(input("Enter hours: "))
        result = hours_to_minutes(hrs)
        print(f"{hrs} hours is equal to {result} minutes.")
    elif option == 2:
        secs = float(input("Enter seconds: "))

        while secs < 60:
            secs = float(input("Enter valid seconds not less than 60: "))

        result = seconds_to_minutes(secs)
        print(f"{secs} seconds is equal to {result} minutes.")
    else:
        print("Invalid input")


if __name__ == "__main__":
    main()
