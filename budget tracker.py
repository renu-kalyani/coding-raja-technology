class BudgetTracker:
    def __init__(self):
        self.balance = 0
        self.income = []
        self.expenses = []

    def add_income(self, amount, description):
        self.income.append({"amount": amount, "description": description})
        self.balance += amount
        print("Income added successfully!")

    def add_expense(self, amount, description):
        self.expenses.append({"amount": amount, "description": description})
        self.balance -= amount
        print("Expense added successfully!")

    def view_balance(self):
        print(f"Your current balance: ${self.balance}")

    def view_summary(self):
        print("\n--- Budget Summary ---")
        print("Income:")
        for inc in self.income:
            print(f"  - {inc['description']}: ${inc['amount']}")
        print("Expenses:")
        for exp in self.expenses:
            print(f"  - {exp['description']}: ${exp['amount']}")
        self.view_balance()


def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\n--- Personal Budget Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Current Balance")
        print("4. View Budget Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter the amount of income: "))
            description = input("Enter a description for the income: ")
            budget_tracker.add_income(amount, description)
        elif choice == "2":
            amount = float(input("Enter the amount of expense: "))
            description = input("Enter a description for the expense: ")
            budget_tracker.add_expense(amount, description)
        elif choice == "3":
            budget_tracker.view_balance()
        elif choice == "4":
            budget_tracker.view_summary()
        elif choice == "5":
            print("Exiting the budget tracker...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
