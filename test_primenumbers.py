""" Test prime numbers"""

import unittest

from gen_primes import gen_primes



class GenPrimesTests(unittest.TestCase):

    def setUp(self):
        """ Gives all test cases access to an instance of the GenPrimesTests """
        self.GenPrimesTests = GenPrimesTests()


    def test_isprime(n):
    '''check if integer n is a prime'''

        # make sure n is a positive integer
        n = abs(int(n))

        # 0 and 1 are not primes
        if n < 2:
            return False

        # 2 is the only even prime number
        if n == 2: 
           return True    

       # all other even numbers are not primes
        if not n & 1: 
            return False

    def test_input_is_int(self):

		gen_primes("1000")

        self.assertRaises(ValueError, 'Only positive integers are allowed as input')
     
    def test_input_is_greater_than_one(self):
        gen_primes= n
    	return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
    	
    
