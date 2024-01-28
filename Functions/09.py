"""
Write a function called check-season,
it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
"""


def set_month():
    month = input("Enter month (January, February, etc.): ")
    return month


def check_season(month):
    if month in ["December", "January", "February"]:
        return "It's winter! Time for bulky clothes :("
    elif month in ["March", "April", "May"]:
        return "It's spring :D"
    elif month in ["June", "July", "August"]:
        return "It's summer ;) Enjoy summer holidays )"
    elif month in ["September", "October", "November"]:
        return "Autumn... Again school :("
    else:
        return "I don't know this month. Maybe you have made a spelling mistake."


def print_season(answer):
    print(answer)


def main():
    month = set_month()
    season = check_season(month)
    print_season(season)


if __name__ == "__main__":
    main()
