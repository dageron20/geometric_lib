import unittest
import math


def area(r):
    '''Принимает радиус окружности (r), выводит площадь этой окружности'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает радиус окружности (r), выводит периметр этой окружности'''
    return 2 * math.pi * r


class TestCircleCases(unittest.TestCase):
	'''area'''
	def test_area_zero(self):
		res = area(0)
		self.assertEqual(res, 0)

	def test_area_big_data(self):
		res = area(555555555555555555555555555555555555555555555)
		self.assertEqual(res, 9.69627362219072e+89)

	def test_area_real_big_data(self):
		res = area(555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555)
		self.assertEqual(res, 9.696273622190719e+269)
    
	def test_area_minus_data(self):
		res = area(-5)
		self.assertEqual(res, 0)
    
	def test_area_word(self):
		res = area(cccc)
		self.assertEqual(res, 0)
    
	def test_area_no_symb(self):
		res = area()
		self.assertEqual(res, 0)

	def test_area_too_many(self):
		res = area(5, 13, 45)
		self.assertEqual(res, 78,53981633974483)

	'''perimeter'''
    
	def test_perimeter_zero(self):
		res = perimeter(0)
		self.assertEqual(res, 0)
    
	def test_perimeter_big_data(self):
		res = perimeter(555555555555555555555555555555555555555555555)
		self.assertEqual(res, 3.490658503988659e+45)
    
	def test_perimeter_real_big_data(self):
		res = perimeter(555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555)
		self.assertEqual(res, 3.490658503988659e+135)
    
	def test_perimeter_minus_data(self):
		res = perimeter(-5)
		self.assertEqual(res, 0)
    
	def test_perimeter_word(self):
		res = perimeter(сссс)
		self.assertEqual(res, 0)
    
	def test_perimeter_no_symb(self):
		res = perimeter()
		self.assertEqual(res, 0)

	def test_perimeter_too_many(self):
		res = area(5, 13, 45)
		self.assertEqual(res, 31.41592653589793)
