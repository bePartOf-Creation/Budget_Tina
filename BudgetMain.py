from Assignment.BudgetTina.BudgetApp import *

food = BudgetCategory("Food")
transport = BudgetCategory("Transport")
clothing = BudgetCategory("Clothing")

food.transfer_funds(4000, transport)
food.withdrawal_fund(2000, "A bag of Garri")
food.withdrawal_fund(1500, "One Sack Of Salt")
food.remainBalanceAfterExpense()

food.transfer_funds(5000, clothing)
clothing.withdrawal_fund(1500, "A pair of Jeans")
clothing.withdrawal_fund(3500, "2 Pairs If Tops")
clothing.remainBalanceAfterExpense()


def main():
    print(food)
    print(food.display_expenses())
    print(food.remainBalanceAfterExpense())
    print(clothing.display_expenses())
    print(clothing.remainBalanceAfterExpense())


if __name__ == '__main__':
    main()
