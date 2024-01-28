"""
Write a function called calculate_slope which return the slope of a linear equation
"""


def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        print("Error: Division by zero. The slope is undefined.")
        return None
    slope = (y2 - y1) / (x2 - x1)
    return slope


def main():
    x1, y1 = 1, 2
    x2, y2 = 3, 4
    slope = calculate_slope(x1, y1, x2, y2)
    if slope is not None:
        print(
            f"The slope of the line passing through ({x1}, {y1}) and ({x2}, {y2}) is: {slope}"
        )


if __name__ == "__main__":
    main()
