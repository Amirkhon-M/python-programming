class Calculator:
    def __init__(self):
        pass

    def add(self, a: float, b: float):
        return a + b
    
    def subtract(self, a: float, b: float):
        return a - b
    
    def multiply(self, a: float, b: float):
        return a * b
    
    def divide(self, a: float, b: float):
        return a / b
    
calc = Calculator()

operation = input("Choose action (+, -, *, /): ")

def get_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

a = get_float_input("Enter first number: ")
b = get_float_input("Enter second number: ")

result = None
if operation == '+':
    result = calc.add(a, b)
elif operation == '-':
    result = calc.subtract(a, b)
elif operation == '*':
    result = calc.multiply(a, b)
elif operation == '/':
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = calc.divide(a, b)
else:
    print("Invalid operation selected.")

if result is not None:
    print(f"The result is: {result}")
