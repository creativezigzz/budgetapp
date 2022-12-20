import sys
from unittest import main

import budget
from budget import Category
import argparse
import itertools


def get_category(name):
    if name in cat_name_dir.keys():  # If the category is in the list of category
        index = cat_name_dir[name]  # Take the index
        return [cat_list[index], index]  # Return the category and the index


def display_menu():
    menu = "{:>20}Menu{:<20}\n".format("-" * 8, '-' * 8)
    menu += "{:>12}{:^20}\n".format("1.", "Add category")
    menu += "{:>12}{:^20}\n".format("2.", "Deposit")
    menu += "{:>12}{:^20}\n".format("3.", "Withdraw")
    menu += "{:>12}{:^20}\n".format("4.", "See all the category")
    menu += "{:>12}{:^20}\n".format("5.", "Transfer")
    menu += "{:>12}{:^20}\n".format("6.", "Create chart")
    menu += "{:>12}{:^20}\n".format("7.", "How to use")
    menu += "{:>12}{:^20}\n".format("8.", "Exit")
    print(menu)

    menu_choice = input("Enter the number of your choice : ")

    if menu_choice == '1':
        cat_name = input("Enter the name for the category :")
        cat = Category(cat_name)
        cat_list.append(cat)
        cat_name_dir[cat_name] = next(count)  # saving the index of the category
        print("Success\n")
        ok = input("Press any Return key to continue to menu")
        display_menu()
    elif menu_choice == '2':
        dep_total = float(input("Enter the amount you would like to deposit (only positive amount) :"))
        if dep_total < 0:
            print("Incorrect amount\n")
        else:
            description = input('Add description of deposit :')
            cat_look = input("Enter the name of the category where you want to add this money :")
            cat = get_category(cat_look)
            if isinstance(cat[0], Category):
                cat[0].deposit(dep_total, description)  # Make the deposit
                cat_list[cat[1]] = cat[0]  # Updating the list with the enw category
                print("Deposit done\n")
                print(cat[0].get_balance())
            else:
                print("None existing category with this name\n")
        ok = input("Press any Return key to continue to menu")
        display_menu()
    elif menu_choice == '3':
        with_total = float(input("Enter the amount you would like to withdraw (only positive amount),\n "
                                 "if the amount is superior to what you have in your category, nothing will happen :"))
        if with_total < 0:
            print("Incorrect amount\n")
        else:
            description = input('Add description of withdraw : ')
            cat_look = input("Enter the name of the category where you want to remove this money :")
            cat = get_category(cat_look)
            if isinstance(cat[0], Category):
                if cat[0].withdraw(with_total, description):  # Make the withdrawal
                    print("Withdraw done\n")
                    cat_list[cat[1]] = cat[0]  # Updating the list with the enw category
                    print(cat[0].get_balance())
                else:
                    print("Not enough fund :( \n")
            else:
                print("None existing category with this name\n")
        ok = input("Press any Return key to continue to menu")
        display_menu()
    elif menu_choice == '4':
        for cat in cat_list:
            print(cat)
        ok = input("Press any Return key to continue to menu")
        display_menu()

    elif menu_choice == '5':
        print("First you need to choose the category where you will make your withdrawal, "
              "then you'll choose the category where you want to transfer the money\n")
        cat_name = input("Category where you will withdraw the money :")
        cat_withdraw = get_category(cat_name)
        if isinstance(cat_withdraw[0], Category):
            cat_name = input("Category that will get the transfer :")
            cat_transfer = get_category(cat_name)
            if isinstance(cat_transfer[0], Category):
                with_total = float(input("Enter the amount you would like to withdraw (only positive amount),\n "
                                         "if the amount is superior to what you have in your transfer category,"
                                         " nothing will happen :"))
                if with_total < 0:
                    print("Incorrect amount\n")
                else:
                    if cat_withdraw[0].transfer(with_total, cat_transfer[0]):
                        print()
                        cat_list[cat_withdraw[1]] = cat_withdraw[0]
                        cat_list[cat_transfer[1]] = cat_transfer[0]
                        print("Transfer done\n")

            else:
                print("None existing category with this name\n")
        else:
            print("None existing category with this name\n")
        ok = input("Press any Return key to continue to menu")
        display_menu()
    elif menu_choice == '6':
        print(budget.create_spend_chart(cat_list))
        with open("chart.txt", 'w+') as file:
            file.write(budget.create_spend_chart(cat_list))
            for cat in cat_list:
                file.write(str(cat))
        ok = input("Press any Return key to continue to menu")
        display_menu()
    elif menu_choice == '7':
        print("You can use this tool create a spend chart that will show you how much percentage "
              "you spent your money in each category (up to 4).\n "
              "First step will be to create a new category, then add it directly the first deposit of how much "
              "you'll be spending this month.\n"
              "Then you can either withdraw the money and tell and what object you use "
              "this money or you can also transfer the money to another account."
              "They cannot be more than 4 category"
              "Thanks for using my Tool management")
        ok = input("Press any Return key to continue to menu")
        display_menu()
    elif menu_choice == '8':
        print("Bye and thanks for using me")
        sys.exit()
    else:
        print("Wrong choice")
        ok = input("Press any Return key to continue to menu")
        display_menu()


if __name__ == '__main__':
    # # Run unit tests automatically
    parser = argparse.ArgumentParser(description="Money management tool where u can enter and create category and see"
                                                 "where you spend all your money.")
    parser.add_argument('-m', '--menu', action='store_true',
                        help="Show the menu where the user can interact and add the category")

    arg = parser.parse_args()

    count = itertools.count()
    cat_list = []  # The list containing all the category to make chart
    cat_name_dir = {}  # The list containing all the name of category existing
    if arg.menu:
        display_menu()
    else:
        sys.exit()
    # Uncomment to run the test
