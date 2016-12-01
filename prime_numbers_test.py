# Prime number generator test cases.

import unittest
from prime_numbers import prime_numbers

class TestCalculator(unittest.TestCase):
	
	# Test if function correctly returns prime numbers. 
	def test_prime_numbers(self):
		self.assertEqual(prime_numbers.prime_numbers(20), [2, 3, 5, 7, 11, 13, 17, 19])

	# Test if function returns error if number less than 2 entered.
	def test_less_than_two(self):
		self.assertEqual(prime_numbers.prime_numbers(1))

	# Test if function returns error if wrong type passed to function.
	def test_invalid_type(self):
		self.assertEqual(prime_numbers.prime_numbers("String"))
