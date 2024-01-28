"""
Employee Payroll: Design a program that calculates employee payroll, including
basic salary, overtime pay, and deductions. Use functions to compute each
component.
"""


def get_basic_salary():
    return 250


def calculate_overtime_pay(overtime_rate):
    hours_worked = float(input("Enter overtime work in hours format: "))
    return overtime_rate * hours_worked


def add_deduction(current_salary):
    deduction = float(input("Enter deduction amount: "))
    return current_salary - deduction


def menu():
    basic_salary = get_basic_salary()
    print(f"Basic salary is: {basic_salary}$")

    print("1. Pay for overtime\n2. Add deduction")
    option = int(input("Option: "))

    if option == 1:
        overtime_pay = calculate_overtime_pay(10)
        print(f"You get {overtime_pay}$ for overtime")
    elif option == 2:
        basic_salary_after_deduction = add_deduction(basic_salary)
        print(f"Salary after deduction: {basic_salary_after_deduction}$")


if __name__ == "__main__":
    menu()
