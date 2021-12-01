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


def create_spend_chart(categories):
    pass
