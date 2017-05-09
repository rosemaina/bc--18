""" Demonstrates virtual wallet """


class Wallet(object):
    """ Defines blue print for digital wallet """

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        """ Checks that the deposit adds money to the wallet
            1. Get amount to be deposotited
            2. Updates balance with amount
            3. Output= updated balance """

            
        if not isinstance(amount,int):
            return "Numbers only please"
        self.balance += amount
        return self.balance

    self.wallet.balance = 0
    self.assertEqual(self.wallet.deposit(1000))
    self.assertEqual(self.wallet.deposit(500))   

    def withdraw(self):
        """ Withdraws money from wallet """