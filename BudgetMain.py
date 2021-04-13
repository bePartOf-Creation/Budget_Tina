from Assignment.BudgetTina.BudgetApp import *

food = BudgetCategory("Food")
transport = BudgetCategory("Transport")

food.transfer_funds(4000, transport)
food.withdrawal_fund(2000, "A bag of Garri")
food.withdrawal_fund(1500, "One Sack Of Salt")


def main():
    print(food)
    print(food.display_expenses())


if __name__ == '__main__':
    main()
