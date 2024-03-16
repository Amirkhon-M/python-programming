"""
Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income,
total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its
description. The same goes for expenses.
"""

class PersonAccount:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.incomes = {}
        self.expenses = {}

    def add_income(self, amount, description):
        self.incomes[description] = amount

    def add_expense(self, amount, description):
        self.expenses[description] = amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_info(self):
        return f"\nFirst name: {self.fname}\nLast name: {self.lname}\nTotal Income: {self.total_income()}\nTotal Expense: {self.total_expense()}"

    def account_balance(self):
        return self.total_income() - self.total_expense()


def main():
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    person = PersonAccount(f_name, l_name)

    while True:
        choice = input("\n[1] Add income\n"
                       "[2] Add expense\n"
                       "[3] Account information\n"
                       "[4] Balance information\n"
                       "[q] Quit ")
        if choice == '1':
            amount = float(input("Enter income amount: "))
            description = input("Enter income description: ")
            person.add_income(amount, description)
            print("Income added successfully!")
        elif choice == '2':
            amount = float(input("\nEnter expense amount: "))
            description = input("Enter expense description: ")
            person.add_expense(amount, description)
            print("\nExpense added successfully!")
        elif choice == '3':
            print(person.account_info())
        elif choice == '4':
            print(f"\nCurrent account balance: {person.account_balance()}")
        elif choice.lower() == 'q':
            break
        else:
            print("\nInvalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
