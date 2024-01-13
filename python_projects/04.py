"""
Write a code which gives grade to students according to theirs score
"""


def result(score: int):
    if score >= 80:
        print("Your grade is A!\nGood job!")
    elif 70 <= score <= 79:
        print("Your grade is B! \nKeep it up!")
    elif 60 <= score <= 69:
        print("Your grade is C! \nStill nice!")
    elif 50 <= score <= 59:
        print("Your grade is D! \nYou should study harder!")
    else:
        print("Your grade is F! :(")


def main():
    score = int(input("Enter the score(0-100): "))
    while score < 0 or score > 100:  # Use 'or' to validate the score range
        print("Invalid score. Please enter a score between 0 and 100.")
        score = int(input("Enter the score(0-100): "))
    result(score)


if __name__ == "__main__":
    main()
