import budget
from budget import Category
from budget import create_spend_chart
from unittest import main

if __name__ == '__main__':
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.deposit(500, "cool deposit")
    food.withdraw(10, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())
    clothing = budget.Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    auto = budget.Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)

    print(food)
    print(clothing)

    print(create_spend_chart([food, clothing, auto]))

    # # Run unit tests automatically
    main(module='test_module', exit=False)
