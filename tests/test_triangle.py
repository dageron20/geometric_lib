import unittest
import math

def area(a, b, c):
    '''Принимает стороны треугольника (a, b и c), возвращает площадь треугольника'''
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def perimeter(a, b, c):
    '''Приниаем стороны треугольника (a, b и c), возвращает периметр треугольника'''
    return a + b + c

class TestCircleCases(unittest.TestCase):
	'''area'''
	def test_area_zero(self):
		res = area(0, 4, 5)
		self.assertEqual(res, 0)

	def test_area_big_data(self):
		res = area(555555555555555555555555555555555555555555555, 555555555555555555555555555555555555555555555, 555555555555555555555555555555555555555555555)
		self.assertEqual(res, 1.3364589564574667e+89)

	def test_area_real_big_data(self):
		res = area(555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555, 555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555, 555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555)
		self.assertEqual(res, 0)
    
	def test_area_minus_data(self):
		res = area(-5, -4, -3)
		self.assertEqual(res, 0)
    
	def test_area_word(self):
		res = area("cccc", "aeaea", "asddas")
		self.assertEqual(res, 0)
    
	def test_area_no_symb(self):
		res = area()
		self.assertEqual(res, 0)

	def test_area_too_many(self):
		res = area(5, 13, 45, 1)
		self.assertEqual(res, 63)

	def test_area_arr(self):
		res = area([5, 4, 3])
		self.assertEqual(res, 6)

	def test_area_arr(self):
		res = area(5, 13, 45)
		self.assertEqual(res, null)

	'''perimeter'''
    
	def test_perimeter_zero(self):
		res = perimeter(0)
		self.assertEqual(res, 0)
    
	def test_perimeter_big_data(self):
		res = perimeter(555555555555555555555555555555555555555555555, 555555555555555555555555555555555555555555555, 555555555555555555555555555555555555555555555)
		self.assertEqual(res, 1666666666666666666666666666666666666666666665)
    
	def test_perimeter_real_big_data(self):
		res = perimeter(555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555, 555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555, 555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555)
		self.assertEqual(res, 1666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666665)
    
	def test_perimeter_minus_data(self):
		res = perimeter(-5, -4, -3)
		self.assertEqual(res, 0)
    
	def test_perimeter_word(self):
		res = perimeter("сссс", "aeaea", "bbbbbbbb")
		self.assertEqual(res, 0)
    
	def test_perimeter_no_symb(self):
		res = perimeter()
		self.assertEqual(res, 0)

	def test_perimeter_too_many(self):
		res = area(5, 13, 45, 1)
		self.assertEqual(res, 63)

	def test_area_arr(self):
		res = area([5, 4, 3])
		self.assertEqual(res, 12)
