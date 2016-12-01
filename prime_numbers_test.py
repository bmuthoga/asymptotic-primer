# Prime number generator test cases.

import unittest
from prime_numbers import prime_numbers

class TestPrimeGenerator(unittest.TestCase):
	
	# Test if function correctly returns prime numbers. 
	def test_prime_numbers(self):
		self.assertEqual(prime_numbers.prime_numbers(20), [2, 3, 5, 7, 11, 13, 17, 19])

	# Test if function returns error if number less than 2 entered.
	def test_less_than_two(self):
		self.assertEqual(prime_numbers.prime_numbers(1), "No prime number existing for given input.")

	# Test if function returns error if wrong type passed to function.
	def test_invalid_type(self):
		self.assertEqual(prime_numbers.prime_numbers("String"), "Only integers allowed.")

	# Test if only positive numbers allowed.
	def test_only_positive(self):
		self.assertEqual(prime_numbers.prime_numbers(-1), "Only positive numbers allowed.")
	
	# Test for empty parameters.
	def test_empty_parameter(self):
		self.assertEqual(prime_numbers.prime_numbers(), "No number entered.")

	# Test for 100.
	def test_one_hundred(self):
		self.assertEqual(prime_numbers.prime_numbers(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

	# Test for 5.
	def test_five(self):
		self.assertEqual(prime_numbers.prime_numbers(5), [2, 3, 5])

	# Test for 50.
	def test_fifty(self):
		self.assertEqual(prime_numbers.prime_numbers(50), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])

	# Test for 2.
	def test_two(self):
		self.assertEqual(prime_numbers.prime_numbers(2), [2])

	# Test for 1.
	def test_one(self):
		self.assertEqual(prime_numbers.prime_numbers(1), "No prime number existing for given input.")