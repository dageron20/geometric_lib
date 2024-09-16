import unittest
import math

def area(a, b):
    '''Принимает стороны прямоугольника (a и b), возвращает площадь прямоугольника'''
    return a * b


def perimeter(a, b):
    '''Принимает стороны прямоугольника (a и b), возвращает периметр прямоугольника '''
    return (a + b) * 2


class TestCircleCases(unittest.TestCase):
	'''area'''
	def test_area_zero(self):
		res = area(0, 5)
		self.assertEqual(res, 0)

	def test_area_big_data(self):
		res = area(555555555555555555555555555555555555555555555, 555555555555555555555555555555555555555555555)
		self.assertEqual(res, 308641975308641975308641975308641975308641974691358024691358024691358024691358024691358025)

	def test_area_real_big_data(self):
		res = area(555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555, 555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555)
		self.assertEqual(res, 308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641974691358024691358024691358024691358024691358024691358024691358024691358024691358024691358024691358024691358024691358024691358024691358025)
    
	def test_area_minus_data(self):
		res = area(-5, 5)
		self.assertEqual(res, 0)
    
	def test_area_word(self):
		res = area(cccc, aeaea)
		self.assertEqual(res, 0)
    
	def test_area_no_symb(self):
		res = area()
		self.assertEqual(res, 0)

	def test_area_too_many(self):
		res = area(5, 13, 45)
		self.assertEqual(res, 65)

	def test_area_arr(self):
		res = area([5, 5])
		self.assertEqual(res, 25)

	'''perimeter'''
    
	def test_perimeter_zero(self):
		res = perimeter(0, 2)
		self.assertEqual(res, 4)
    
	def test_perimeter_big_data(self):
		res = perimeter(555555555555555555555555555555555555555555555, 2)
		self.assertEqual(res, 1111111111111111111111111111111111111111111114)
    
	def test_perimeter_real_big_data(self):
		res = perimeter(555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555, 555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555)
		self.assertEqual(res, 2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220)
    
	def test_perimeter_minus_data(self):
		res = perimeter(-5, 7)
		self.assertEqual(res, 0)
    
	def test_perimeter_word(self):
		res = perimeter(сссс, aeaea)
		self.assertEqual(res, 0)
    
	def test_perimeter_no_symb(self):
		res = perimeter()
		self.assertEqual(res, 0)

	def test_perimeter_too_many(self):
		res = area(5, 13, 45)
		self.assertEqual(res, 31.41592653589793)

	def test_area_arr(self):
		res = area([5, 5])
		self.assertEqual(res, 20)
