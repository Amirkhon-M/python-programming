"""
Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
Write a function which converts °C to °F, *convert_celsius_to-fahrenheit*.
"""


def menu():
    print("1. Convert °C to °F\n2. Convert °F to °C")
    option = int(input("Option: "))

    if option == 1:
        celsius = float(input("Enter °C: "))
        result = convert_celsius_to_fahrenheit(celsius)
    elif option == 2:
        fahrenheit = float(input("Enter °F: "))
        result = convert_fahrenheit_to_celsius(fahrenheit)
    else:
        print("Invalid option")
        return

    print(f"The result is {result}")


def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    menu()
