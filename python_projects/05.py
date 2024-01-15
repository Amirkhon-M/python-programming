def analyze_month(month):
    if month in ["January", "December", "February"]:
        season = "Winter"
    elif month in ["March", "April", "May"]:
        season = "Spring"
    elif month in ["June", "July", "August"]:
        season = "Summer"
    elif month in ["September", "October", "November"]:
        season = "Autumn"
    else:
        season = "Invalid month!"
    return season


def get_month_input():
    month = input("Enter the month (January, December, February, etc.): ")
    return month


def main():
    month = get_month_input()
    season = analyze_month(month)

    print(f"Month: {month}")
    print(f"Season: {season}")


if __name__ == "__main__":
    main()
