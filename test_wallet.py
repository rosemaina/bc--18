""" Tests our wallet """

import unittest
from wallet import Wallet


class TestWallet(unittest.TestCase):
    """ Tests Wallet functionality """

    def setUp(self):
        """ Gives all test cases access to an instance of the Wallet """
        self.wallet = Wallet()
        
    def test_deposit_works(self):
        """ Checks that deposit adds money to wallet
            get amount to be deposited"""
        
        self.wallet.balance = 0
        self.assertEqual(self.wallet.deposit(1000),1000)
        self.assertEqual(self.wallet.deposit(500),1500)

        #test input type
    def test_amount_is_number(self):
        self.assertEqual(self.wallet.deposit("1000"),"Numbers only please!!")


if __name__== '__main__':
unittest.main()
