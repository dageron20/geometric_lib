
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
		self.assertEqual(res, 100)

	# наверное нет прямоугольника с отрицательной стороной
	# но нет и прямоугольника с нулевой стороной
	def test_negative_mul(self):
		res = area(24, -10)
		self.assertEqual(res, -240)
		res = area(10, -24)
		self.assertEqual(res, -240)
		res = area(-24, -10)
		self.assertEqual(res, 240)

	def test_float_mul(self):
		res = area(24.24, -10.10)
		self.assertEqual(res, -244.824)

	def test_char_mul(self):
		self.assertRaises(TypeError, lambda: area("24", "10"))

	def test_bool_mul(self):
		res = area(True, True)
		self.assertEqual(res, 1)
		res = area(False, False)
		self.assertEqual(res, 0)

	def test_overflow_mul(self):
		res = area(153092023, 60247241209)
		self.assertEqual(res, 9223372036854775807)
		res = area(-2**32, 2**31)
		self.assertEqual(res, -9223372036854775808)

	def test_zero_sum(self):
		res = perimeter(0, 0)
		self.assertEqual(res, 0)
		res = perimeter(10, 0)
		self.assertEqual(res, 20)
		res = perimeter(0, 10)
		self.assertEqual(res, 20)

	def test_negative_sum(self):
		res = perimeter(24, -10)
		self.assertEqual(res, 28)
		res = perimeter(10, -24)
		self.assertEqual(res, -28)
		res = perimeter(-24, -10)
		self.assertEqual(res, -68)

	def test_float_sum(self):
		res = perimeter(24.24, -10.10)
		self.assertEqual(res, 28.28)

	def test_char_sum(self):
		self.assertRaises(TypeError, perimeter("24", "10"))

	def test_bool_sum(self):
		res = perimeter(True, True)
		self.assertEqual(res, 4)
		res = perimeter(False, False)
		self.assertEqual(res, 0)

	def test_overflow_sum(self):
		res = perimeter(2412930120939012125, 2198755897488375778)
		self.assertEqual(res, 9223372036854775806)
		res = perimeter(-1582384989125564907, -3029301029301822997)
		self.assertEqual(res, -9223372036854775808)

def area(a, b):
	''' Принимает значения a и b, возвращает их произведение (площадь) '''
	return a * b

def perimeter(a, b):
	''' Принимает значения a и b, возвращает их сумму, умноженную на 2 (периметр) '''
	return 2 * (a + b)