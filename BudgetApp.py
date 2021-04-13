from Assignment.BudgetTina.initials import *


class BudgetCategory:
    """A simple attempt to model a Budget."""

    def __init__(self, name):
        """Initialize balance attributes and Keep track of expense in a list"""
        self.name = name
        self.balance = self.initial_cash = budget_amount
        self.keep_expense = list()

    def __str__(self, ):
        return (f"\nWelcome to Budget_Tina..\n"
                f"******* My Budget ******* \nBudget Amount :{budget_amount}\n"
                f"Spend It Wisely..\n")

    def validate_funds(self, amount):
        if self.balance > amount:
            return True
        return False

    def deposit_funds(self, funds, expense_description):
        """Simulating a deposit function."""
        self.balance += funds
        self.keep_expense.append(
            {
                "expense_description": expense_description,
                "amount": funds
            }
        )

    def withdrawal_fund(self, funds, expense_description):
        """Simulating a withdrawal function."""
        self.validate_funds(amount=funds)
        self.balance -= funds
        self.keep_expense.append(
            {
                "expense_description": expense_description,
                "amount": funds
            }
        )

    def transfer_funds(self, funds, otherBudgetCategory):
        """Simulating a transfer of funds from a budget category to another."""
        if self.validate_funds(funds):
            self.balance -= funds
            otherBudgetCategory.balance += funds
            self.keep_expense.append(
                {
                    "expense_description": "Transfer from " + self.name + " to " + otherBudgetCategory.name,
                    "amount": 0
                }
            )
            return True
        print(f"Insufficient Funds. Cannot Transfer To {otherBudgetCategory.name} ")
        return False

    def total_expenses(self):
        total_Budget = 0
        for item in self.keep_expense:
            total_Budget += item["amount"]
        return total_Budget

    def display_expenses(self):
        global expenses, exp_amount, category_type
        category_type = self.name
        print(f"******* {category_type} ****** \n"
              f"Initial Cash : {self.initial_cash:,d} \n")
        for item in self.keep_expense:
            expenses = item["expense_description"]
            exp_amount = item["amount"]
            print(f"{expenses} : {exp_amount:,d}")
        print(f"Total Expenses : {self.total_expenses():,d} ")
