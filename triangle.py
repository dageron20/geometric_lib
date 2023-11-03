
import unittest

class RectangleTestCase(unittest.TestCase):
	def test_zero_mul(self):
		res = area(10, 0)
		self.assertEqual(res, 0)
		res = area(0, 10)
		self.assertEqual(res, 0)
		res = area(0, 0)
		self.assertEqual(res, 0)

	def test_square_mul(self):
		res = area(10, 10)
		self.assertEqual(res, 50)

	def test_negative_mul(self):
		res = area(24, -10)
		self.assertEqual(res, -120)
		res = area(10, -24)
		self.assertEqual(res, -120)
		res = area(-24, -10)
		self.assertEqual(res, 120)

	def test_float_mul(self):
		res = area(24.24, -10.10)
		self.assertEqual(res, -122.412)

	def test_overflow_mul(self):
		res = area(153092023, 60247241208)
		self.assertEqual(res, 4611686018350841892)
		res = area(-2**32, 2**31)
		self.assertEqual(res, -4611686018427387904)

	def test_zero_sum(self):
		res = perimeter(0, 0, 0)
		self.assertEqual(res, 0)
		res = perimeter(10, 0, 10)
		self.assertEqual(res, 20)
		res = perimeter(0, 10, 10)
		self.assertEqual(res, 20)

	def test_negative_sum(self):
		res = perimeter(24, -10, -42)
		self.assertEqual(res, -28)
		res = perimeter(10, -24, 42)
		self.assertEqual(res, 28)
		res = perimeter(-24, -10, -42)
		self.assertEqual(res, -76)

	def test_float_sum(self):
		res = perimeter(24.24, -10.10, 42.42)
		self.assertEqual(res, 56.56)

	def test_overflow_sum(self):
		res = perimeter(860234565451967870, 3965625676426056380, 4397511794976751557)
		self.assertEqual(res, 9223372036854775807)
		res = perimeter(-3164769978251129814, -3042078024062405980, -3016524034541240014)
		self.assertEqual(res, -9223372036854775808)

def area(a, h):
	''' Принимает значения a и h, вовращает их произведение, деленное на 2 (площадь) '''
	return a * h / 2

def perimeter(a, b, c):
	''' Принимает значения a, b и c, возвращает их сумму (периметр) '''
	return a + b + c