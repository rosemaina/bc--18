""" |Returns min and max values respectively in a list or array"""

def max_min(n):

	n.sort();

	min = n[1]

	max = n[-3]

	newarry = []

	newarry.append(min)

	newarry.append(max)

	return newarry

#output
"""Here the output will be [9,57]"""

print(max_min([57, 100, 9, 2, 68, 23]))