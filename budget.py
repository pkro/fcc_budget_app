from copy import deepcopy


def make_title(title):
    asterisks = '*' * ((30 - len(title)) // 2)
    return f'{asterisks}{title}{asterisks}'


def float_to_amount(num):
    amount = str(num).split(".")
    if len(amount) == 1:
        amount.append('')

    return f'{amount[0]}.{amount[1].rjust(2, "0")}'


def justify(description, amount):
    return f'{description[:23].ljust(23, " ")}{float_to_amount(amount)[:7].rjust(7, " ")}'


class Category:
    def __init__(self, category):
        self.category = category
        self.ballance = 0.0
        self.ledger = []

    def deposit(self, amount, description=""):
        """A deposit method that accepts an amount and description. If no
        description is given, it should default to an empty string. The method
        should append an object to the ledger list in the form of {"amount":
        amount, "description": description}.

        Args: amount ([type]): [description] description (str, optional):
            [description]. Defaults to "".

        Returns: [type]: [description]
        """
        self.ballance += amount
        self.ledger.append({"amount": amount, "description": description})
        return self

    def withdraw(self, amount, description=""):
        """A withdraw method that is similar to the deposit method, but the amount
          passed in should be stored in the ledger as a negative number. If there are not
          enough funds, nothing should be added to the ledger. This method should return
          True if the withdrawal took place, and False otherwise.
        """
        if not self.check_funds(amount):
            return False

        self.ballance -= amount
        self.ledger.append({"amount":
                            -amount, "description": description})
        return True

    def get_balance(self):
        """A get_balance method that returns the current balance of the budget
        category based on the deposits and withdrawals that have occurred."""
        return self.ballance

    def transfer(self, amount, category):
        """A transfer method that accepts an amount and another budget category as
        arguments. The method should add a withdrawal with the amount and the
        description "Transfer to [Destination Budget Category]". The method should
        then add a deposit to the other budget category with the amount and the
        description "Transfer from [Source Budget Category]". If there are not
        enough funds, nothing should be added to either ledgers. This method
        should return True if the transfer took place, and False otherwise."""
        if not self.check_funds(amount):
            return False

        balance_copy = self.ballance
        ledger_copy = deepcopy(self.ledger)
        try:
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
        except:
            self.ballance = balance_copy
            self.ledger = ledger_copy
            return False

        return True

    def check_funds(self, amount):
        """A check_funds method that accepts an amount as an argument. It returns
        False if the amount is greater than the balance of the budget category and
        returns True otherwise. This method should be used by both the withdraw
        method and transfer method."""
        if self.ballance - amount < 0:
            return False
        return True

    def __str__(self):
        """When the budget object is printed it should display:
        A title line of 30 characters where the name of the category is centered in a line of * characters.
        A list of the items in the ledger. Each line should show the description
        and amount. The first 23 characters of the description should be
        displayed, then the amount. The amount should be right aligned, contain
        two decimal places, and display a maximum of 7 characters.
        A line displaying the category total.
        Here is an example of the output:

        *************Food*************
        initial deposit        1000.00
        groceries               -10.15
        restaurant and more foo -15.89
        Transfer to Clothing    -50.00
        Total: 923.96
        """
        lines = []
        lines.append(make_title(self.category))
        for item in self.ledger:
            # these are by order, not by name like in js destructuring!
            amount, description = item.values()
            lines.append(justify(description, amount))
        lines.append(f"Total: {self.ballance}")
        return "\n".join(lines)


def create_spend_chart(iterable):
    """Besides the Category class, create a function (ouside of the class) called
    create_spend_chart that takes a list of categories as an argument. It should
    return a string that is a bar chart.

    The chart should show the percentage spent in each category passed in to the
    function. The percentage spent should be calculated only with withdrawals and
    not with deposits. Down the left side of the chart should be labels 0 - 100. The
    "bars" in the bar chart should be made out of the "o" character. The height of
    each bar should be rounded down to the nearest 10. The horizontal line below the
    bars should go two spaces past the final bar. Each category name should be
    vertacally below the bar. There should be a title at the top that says
    "Percentage spent by category".

    Percentage spent by category
    100|
    90|
    80|
    70|
    60| o
    50| o
    40| o
    30| o
    20| o  o
    10| o  o  o
      0| o  o  o
        ----------
        F  C  A
        o  l  u
        o  o  t
        d  t  o
            h
            i
            n
            g
        """
    pass
