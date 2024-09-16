import unittest
import math

def area(a):
    '''Принимает сторону квадрата (a), возвращает площадь квадрата'''
    return a * a


def perimeter(a):
    '''Принимает сторону квадрата (a), возвращает периметр квадрата'''
    return 4 * a

class TestCircleCases(unittest.TestCase):
	'''area'''
	def test_area_zero(self):
		res = area(0)
		self.assertEqual(res, 0)

	def test_area_big_data(self):
		res = area(555555555555555555555555555555555555555555555)
		self.assertEqual(res, 308641975308641975308641975308641975308641974691358024691358024691358024691358024691358025)

	def test_area_real_big_data(self):
		res = area(555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555)
		self.assertEqual(res, 308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641974691358024691358024691358024691358024691358024691358024691358024691358024691358024691358024691358024691358024691358024691358024691358025)
    
	def test_area_minus_data(self):
		res = area(-5)
		self.assertEqual(res, 0)
    
	def test_area_word(self):
		res = area(cccc, aeaea)
		self.assertEqual(res, 0)
    
	def test_area_no_symb(self):
		res = area()
		self.assertEqual(res, 0)

	def test_area_too_many(self):
		res = area(5, 13, 45)
		self.assertEqual(res, 25)

	def test_area_arr(self):
		res = area([5])
		self.assertEqual(res, 25)

	'''perimeter'''
    
	def test_perimeter_zero(self):
		res = perimeter(0)
		self.assertEqual(res, 0)
    
	def test_perimeter_big_data(self):
		res = perimeter(555555555555555555555555555555555555555555555)
		self.assertEqual(res, 2222222222222222222222222222222222222222222220)
    
	def test_perimeter_real_big_data(self):
		res = perimeter(555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555)
		self.assertEqual(res, 2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220)
    
	def test_perimeter_minus_data(self):
		res = perimeter(-5)
		self.assertEqual(res, 0)
    
	def test_perimeter_word(self):
		res = perimeter(сссс, aeaea)
		self.assertEqual(res, 0)
    
	def test_perimeter_no_symb(self):
		res = perimeter()
		self.assertEqual(res, 0)

	def test_perimeter_too_many(self):
		res = area(5, 13, 45)
		self.assertEqual(res, 20)

	def test_area_arr(self):
		res = area([5])
		self.assertEqual(res, 20)
