simport datetime


class MPESA:

    def __init__(self):
        self.name =  input("Please enter the Account Name: ")
        self.number = input("Please enter the Phone Number: ")
        self.balance = 0.0
        self.loan = 0.0
        self.withdrawals = []
        self.deposits = []
        self.loans = []
        print("Dear", self.name, "welcome to MPESA")
        print("Start by depositing some money")


    def showname(self):
        print(self.name)
        return

    def showbalance(self):
        print(self.balance)
        return

    def depositcash(self, amount):
        """
        An MPESA deposit cannot succeed if:
            - The amount given is negative or zero
            - User has a loan ???
        Otherwise we increament the user's balance with the amount
        """

        now = datetime.datetime.now()
        time = now.strftime("%c")
        if amount <= 0:
            print("Dear,", self.name, "You cannot deposit", amount,"amount" )
        else:
            self.balance += amount
            details = {
                "date": time,
                "amount": amount
            }
            self.deposits.append(details)
            print("Dear,", self.name, "You have deposited", amount,"at", time, "new balance is", self.balance)

        return

    def withdrawcash(self, amount):
        """
        A withdrawal only succeeds if:
            - The amount requested is positive
            - The amount requested is less than available deposit balance
        """
        now = datetime.datetime.now()
        time = now.strftime("%c")
        if amount < 0:
            print("Dear,", self.name, "You cannot withdraw", amount,"because it is a negative value" )

        elif amount <= self.balance:
            self.balance -= amount
            details = {
                "date": time,
                "amount": amount
            }
            self.withdrawals.append(details)
            print("Dear,", self.name, "You have have withdrawn", amount, "at", time, "new balance", self.balance)

        else:
            print("Dear,", self.name, "Your balance is", self.balance, "so you cannot withdraw", amount)

        return

    def showdeposits(self):
        if len(self.deposits) >= 1:
            print("Dear", self.name)
            print("------------")
            for item in self.deposits:
                print("On", item['date'], "you deposited", item['amount'])
        else:
            print("Dear", self.name, "You have no deposits")

        return

    def showwithdrawals(self):
        if len(self.withdrawals) >= 1:
            print("Dear", self.name)
            print("------------")
            for item in self.withdrawals:
                print("On", item['date'], "you withdrew", item['amount'])
        else:
            print("Dear", self.name, "You have no withdrawals")

        return

    def giveloan(self):
        """
        Condition for getting a loan:
            - User has made at least 10 deposits.
            - Amount must be more than 50
            - Loan requested must be less than 1/3 of total sum of deposit history
            - User has no deposit balance
            - User has no outstanding loans
            - Loan has an intereset of 10%.
        The loan given is amount of outstanding loan
        list_of_deposits = []
        for deposit in self.deposits:
            list_of_deposits.append(deposit['amount'])
        total_deposits = sum(list_of_deposits)
        """
        amount = int(input("Please enter the Amount: "))
        print(amount)

        if len(self.deposits) < 10:
            print("Failed: You must have deposited at least 10 times")

        elif amount < 50:
            print("Dear, ", self.name, "You cannot withdraw less than 50 bob")

        elif amount * 3 > sum([deposit['amount'] for deposit in self.deposits]):
            print("You don't have enough credit score")

        elif self.balance != 0:
            print("You cannot have a balance before taking a loan")

        elif self.loan != 0:
            print("You have an outstanding loan of ", self.loan)

        else:
            loan_intereset = 0.1*amount
            loan_amount = amount + loan_intereset
            self.loan  += loan_amount
            print("Success: You have received a loan of ",amount,
                  "your outstanding loan balance is ", self.loan)
        return

    def payloan(self, amount):
        """
        Accept loan payment if:
            - amount is larger than 50.
            - user has a loan or else save as deposit
        Amount contributes to loan repayment
        If amount is larger than remaining loan, the remainder is kept as deposit
        """
        now = datetime.datetime.now()
        time = now.strftime("%c")

        if amount < 50:
            print("You must enter an amount more than", amount, "to repay the loan")

        elif not self.loan:

            self.balance += amount
            details = {
                "date": time,
                "amount": amount
            }
            self.deposits.append(details)
            print("Dear,", self.name, "You have no loan balance so", amount,
                  "has been deposited to your account on", time, "Your new balance is", self.balance)

        elif amount > self.loan:
            diff = amount - self.loan
            old_loan = self.loan
            self.loan = 0
            self.balance += diff
            details = {
                "date": time,
                "amount": diff
            }
            self.deposits.append(details)
            print("Dear,", self.name, "you have fully settled your loan of", old_loan, "and the balance of", diff,
                  "has been deposited to your account on", time, "new account balance is", self.balance)
        else:
            self.loan -= amount
            if not self.loan:
                print("Dear,", self.name, "you have fully settled your loan")
            else:
                print("Dear,", self.name, "you have paid", amount,
                      "towards your loan. New loan balance is", self.loan)

        return

    def sendmoney(self, amount, number):
        return None

    def printstatement():
        return None