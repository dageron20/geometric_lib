
import unittest

class RectangleTestCase(unittest.TestCase):
	def test_zero_mul(self):
		res = area(0)
		self.assertEqual(res, 0)

	def test_negative_mul(self):
		res = area(-24)
		self.assertEqual(res, 576)

	def test_float_mul(self):
		res = area(24.24)
		self.assertEqual(res, 587.5776)

	def test_overflow_mul(self):
		res = area(3037000499)
		self.assertEqual(res, 9223372030926249001)

	def test_zero_sum(self):
		res = perimeter(0)
		self.assertEqual(res, 0)

	def test_negative_sum(self):
		res = perimeter(-24)
		self.assertEqual(res, -96)

	def test_float_sum(self):
		res = perimeter(-24.24)
		self.assertEqual(res, -96.96)

	def test_overflow_sum(self):
		res = perimeter(2305843009213693951)
		self.assertEqual(res, 9223372036854775804)

def area(a):
    ''' Принимает значение a, вовращает квадрат a (площадь) '''
    return a * a


def perimeter(a):
    ''' Принимает значение a, возвращает 4a (периметр) '''
    return 4 * a
