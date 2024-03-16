import random

CHARS = "1234567890"


def generate_uuid(length: int = 4) -> str:
    random_chars = [random.choice(CHARS) for _ in range(length)]
    result = "".join(random_chars)
    return result


class Employee:
    def __init__(self, name, rate_per_hour):
        self.ID = generate_uuid()
        self.name = name
        self.rate_per_hour = rate_per_hour

    def display_details(self):
        print(f"Employee ID: {self.ID}")
        print(f"Name: {self.name}")
        print(f"Rate per hour: {self.rate_per_hour}")

    def calculate_monthly_salary(self, hours_worked):
        monthly_salary = self.rate_per_hour * hours_worked
        print(f"Monthly salary of {self.name}: ${monthly_salary:.2f}")


def register_employee():
    name = input("Enter employee name: ")
    rate_per_hour = float(input("Enter rate per hour: "))
    return Employee(name, rate_per_hour)


def main():
    employees = []
    while True:
        print("\nMenu:")
        print("1. Register new employee")
        print("2. Display employee details")
        print("3. Calculate monthly salary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            new_employee = register_employee()
            employees.append(new_employee)
            print("Employee registered successfully!")

        elif choice == "2":
            if not employees:
                print("No employees registered yet.")
            else:
                for idx, emp in enumerate(employees, 1):
                    print(f"\nEmployee {idx} details:")
                    emp.display_details()

        elif choice == "3":
            if not employees:
                print("No employees registered yet.")
            else:
                index = int(input("Enter employee index: ")) - 1
                hours_worked = float(input("Enter hours worked: "))
                employees[index].calculate_monthly_salary(hours_worked)

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
