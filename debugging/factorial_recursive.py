#!/usr/bin/python3
import sys

def factorial(n):
	"""
	Calculate the factorial of a number using recursion.

	Parameters:
	n (int): The number to calculate the factorial of.

	Returns:
	int: The factorial of the number n.
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

# Get the number from command line arguments and calculate its factorial
f = factorial(int(sys.argv[1]))
print(f)
