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
        totamount = 0
        totstr = ""
        for item in self.__ledger:
            des = '{:23}'.format(item["description"])
            amo = '{:>7}'.format(item["amount"])
            totamount += item["amount"]
            totstr += f"{des}{amo}\n"
        return f"{name}\n" \
               f"{totstr}" \
               f"Total: {totamount}"

    @property
    def ledger(self):
        return self.__ledger

    @ledger.setter
    def ledger(self, newledg):
        self.__ledger = newledg

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
        if self.total() < amount:
            return False
        else:
            self.__ledger.append({"amount": -amount, "description": description})
            return True


def create_spend_chart(categories):
    pass
