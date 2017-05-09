#Test to produce the perfect function

def data_type(x):

	# Takes an input and returns a value according to that data type of input

	x_type = type(x)



	# Returns a string with its length

	if x_type == str:

		return len(x)



	# Returns boolean value

	elif x_type == bool:

		return x



	# Compares a string to 100

	elif x_type == int:

		if x == 100:

			return 'Equal to 100'

		elif x < 100:

			return 'Less than 100'

		else:

			return 'more than 100'



	# Returning items in a list. in thsi case the 3rd item

	elif x_type == list:

		try:

			if x[2]:

				return x[2]

		except(IndexError):

			return None

	else:

		return 'no value'





print (data_type([1, 2, 3]))