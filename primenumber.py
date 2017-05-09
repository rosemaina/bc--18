""" Demonstrates prime number function"""

def primes(N):

    prime_numbers = []



def isprime(x):
	for n in range(2, x - 1):
		if x % n == 0:
			return False 

		else:
			return True

	for num in range(2, N + 1):

		if isprime(num):

		    prime_numbers.append(num)

			return prime_numbers


		if N < 0:
			return False

		elif N== 0 and N==1:

		    return False

		elif
			return 'Error'
		  
			pass


print primes(23)