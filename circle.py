
import math
import unittest

class RectangleTestCase(unittest.TestCase):
	def test_zero_area(self):
		res = area(0)
		self.assertEqual(res, 0)

	def test_negative_area(self):
		res = area(24)
		self.assertEqual(res, 1809.5573684677208)
		res = area(-24)
		self.assertEqual(res, 1809.5573684677208)

	def test_float_area(self):
		res = area(24.24)
		self.assertEqual(res, 1845.9294715739218)

	def test_overflow_area(self):
		res = area(1518500249)
		self.assertEqual(res, 7.24401944865036e+18)

	def test_zero_per(self):
		res = perimeter(0)
		self.assertEqual(res, 0)

	def test_negative_per(self):
		res = perimeter(-24)
		self.assertEqual(res, -150.79644737231007)

	def test_float_per(self):
		res = perimeter(24.24)
		self.assertEqual(res, 152.30441184603316)

	def test_overflow_per(self):
		res = perimeter(1152921504606846975)
		self.assertEqual(res, 7.244019458077123e+18)

def area(r):
	''' Принимает значение r, возвращает значение r в квадрате, умноженное на π (площадь) '''
	return math.pi * r * r


def perimeter(r):
	''' Принимает значение r, возвращает r, умноженное на 2π (периметр) '''
	return 2 * math.pi * r

