from operator import itemgetter
from itertools import zip_longest
import math


def roundup(x):
    return int(math.ceil(x / 10.0)) * 10


class CategoryException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class Category(object):
    def __init__(self, name="Empty"):
        self.__name = name
        ledger = []
        self.__ledger = ledger

    def __str__(self):
        name = '{:*^30}'.format(self.__name)
        totstr = ""
        for item in self.__ledger:
            des = '{:.23}'.format('{:23}'.format(item["description"]))
            amo = '{:>7}'.format(item["amount"])
            totstr += f"{des}{amo}\n"
        return f"{name}\n" \
               f"{totstr}" \
               f"Total: {'{:.7}'.format(self.total())}" \
               f"\n \n"

    @property
    def name(self):
        return self.__name

    @property
    def ledger(self):
        return self.__ledger

    def total(self):
        """A method to return the total amount present in the ledger
        PRE:/
        POST:/
        :return: total mount in the ledger
        """
        total = 0
        for item in self.__ledger:
            total += item["amount"]
        return total

    def deposit(self, amount, description=""):
        """Method that accepts an amount and description and add it to the ledger

         PRE: amount must be filled, but the description is optional.
         POST: create a new dictionary entry with the amount and description (if it's only
         the amount then return a empty description) and add it to the ledger of the instance.

        :param amount: Total of the price added
        :param description: A little description of the product
        :return: /
        """
        self.__ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """ Method similar to deposit but it store an negative amount
        PRE: amount is positive. If there are not enough funds, nothing should be added to the ledger.
        POST: This method should return True if the withdrawal took place, and False otherwise.
        RAISE: If amount is negative or equal to zero, then raise an exception.
        :param amount: Total of the priced that will be withdraw from the ledger
        :param description: A little description of the product
        :return: True if the withdrawal took place, False otherwise
        """
        if amount <= 0:
            raise CategoryException("The amount cannot be negative or equal to zéro")
        if not self.check_funds(amount):
            return False
        else:
            self.__ledger.append({"amount": -amount, "description": description})
            return True

    def get_balance(self):
        """Method to print the total amount

        :return: /
        """

        return f"You got {'{:.7}'.format(self.total())}€ on your budget category \n \n"

    def transfer(self, amount, other):
        """Method to transfer a mount from a category to another category
        PRE: Amount must be positive, and other is an existing category
        POST: If there is enough funds in the self.ledger then add a new withdraw with
        a description "Transfer to [other] Budget Categroy" and add a new deposit on other.ledger
        with the same amount and a description : Transfer from [Source Budget Category]".
        If there are not enough funds, nothing should be added to either ledgers.
        RAISE: If amount is negative or equal to zero, then raise an exception.
        :param amount: The amount to transfer
        :param other: The other categroy budget you want to deposit
        :return: True if the operation went well or False if not
        """
        if amount <= 0:
            raise CategoryException("The amount cannot be negative or equal to zéro")
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, f"Transfer to {other.__name} Budget Category")
            other.deposit(amount, f"Transfer from {self.__name} Budget Category")
            return True

    def check_funds(self, amount):
        """Method that check and compare the amount on the current balance and the other amount

        :param amount: The amount that we will compare with the actual funds
        :return: True if amount is lower than the actual balance of the category and returns False otherwise.
        """
        if amount > self.total():
            return False
        return True

    def total_withdraw(self):
        total_withdraw = 0
        for item in self.__ledger:
            if item["amount"] < 0:
                total_withdraw += -(item["amount"])
        return total_withdraw


def create_spend_chart(categories: list = Category):
    """Show the pourcentages spent in each category passed in to the function.
    PRE: The percentage spent should be calculated only with withdrawals and not with deposits.µ
    They can be up to four category.
    POST : Each percentage of category should be rounded down to the nearest 10.
    :param categories: a list of all the Category object that want to be compare
    :return: a string that is the chart.
    """
    finalstring = f"{'{:-^20}'.format('')} \n" \
                  "Percentage spent by category \n" \
                  f"{'{:-^20}'.format('')} \n"
    totalwithdraw = 0
    allcat = []
    for cat in categories:  # counting of each categories
        totalwithdraw += cat.total_withdraw()
    # Creating a new list of dictionary to sort
    for cat in categories:
        percentage = roundup(cat.total_withdraw() / totalwithdraw * 100)
        allcat.append({"categories": cat.name, "percentage_withdrawals": percentage})
    newallcat = sorted(allcat, key=itemgetter('percentage_withdrawals'),
                       reverse=True)  # ou aussi mais moins propre key=lambda k: k['percentage_withdrawals']
    for x in range(100, -10, -10):
        finalstring += f"{'{:3}'.format(x)}|"
        for cat in newallcat:
            if cat["percentage_withdrawals"] > x:
                finalstring += " o"
            else:
                finalstring += "  "
        finalstring += "\n"
    listname = []  # Liste qui contient les différents noms des catégories
    finalstring += f"{'{:-^20}'.format('')} \n"
    for cat in categories:
        listname.append(cat.name)
    # Remplir la liste pour qu'elle contienne 4 éléments
    while (len(listname) < 4):
        listname.append("")
    for item1, item2, item3, item4 in zip_longest(listname[0], listname[1], listname[2], listname[3], fillvalue=" "):
        finalstring += f"{'{:>6}'.format(item1)} {item2} {item3} {item4} \n"
        # for x in newallcat:
        #
        #     finalstring += f"{x['categories'][y]}"
        # finalstring += "\n"
    return finalstring
