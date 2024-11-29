import unittest
import circle
import rectangle
import square
import triangle

class CircleTestCase(unittest.TestCase):

	def test_zero_case(self):
		area_res=circle.area(0)
		per_res=circle.perimeter(0)
		self.assertEqual(area_res, 0)
		self.assertEqual(per_res, 0)

	def test_circle_area(self):
		res_1 = circle.area(5)
		res_2 = circle.area(17)
		self.assertEqual(res_1, 78.53981633974483)
		self.assertEqual(res_2, 907.9202768874503)

	def test_circle_perimeter(self):
		res_1 = circle.perimeter(7)
		res_2 = circle.perimeter(10)
		self.assertEqual(res_1, 43.982297150257104)
		self.assertEqual(res_2, 62.83185307179586)

	def test_negative_case(self):
		area_res=circle.area(-1);
		per_res=circle.perimeter(-1);
		self.assertEqual(area_res, 0)
		self.assertEqual(per_res, 0)

class RectangleTestCase(unittest.TestCase):
	def test_zero_case(self):
		area_res_1 = rectangle.area(5, 0)
		area_res_2 = rectangle.area(0, 5)
		per_res_1 = rectangle.perimeter(7, 0)
		per_res_2 = rectangle.perimeter(0, 6)
		self.assertEqual(area_res_1, 0)
		self.assertEqual(area_res_2, 0)
		self.assertEqual(per_res_1, 0)
		self.assertEqual(per_res_2, 0)

	def test_rectangle_area(self):
		res_1 = rectangle.area(5, 14)
		res_2 = rectangle.area(13, 25)
		self.assertEqual(res_1, 70)
		self.assertEqual(res_2, 325)

	def test_rectangle_perimeter(self):
		res_1 = rectangle.perimeter(5, 14)
		res_2 = rectangle.perimeter(13, 25)
		self.assertEqual(res_1, 38)
		self.assertEqual(res_2, 76)

	def test_negative_case(self):
		area_res_1 = rectangle.area(5, -1)
		area_res_2 = rectangle.area(-1, 5)
		per_res_1 = rectangle.perimeter(7, -1)
		per_res_2 = rectangle.perimeter(-1, 6)
		self.assertEqual(area_res_1, 0)
		self.assertEqual(area_res_2, 0)
		self.assertEqual(per_res_1, 0)
		self.assertEqual(per_res_2, 0)

class SquareTestCase(unittest.TestCase):
	def test_zero_case(self):
		area_res = square.area(0)
		per_res = square.perimeter(0)
		self.assertEqual(area_res, 0)
		self.assertEqual(per_res, 0)

	def test_square_area(self):
		res_1 = square.area(5)
		res_2 = square.area(13)
		self.assertEqual(res_1, 25)
		self.assertEqual(res_2, 169)

	def test_square_perimeter(self):
		res_1 = square.perimeter(14)
		res_2 = square.perimeter(25)
		self.assertEqual(res_1, 56)
		self.assertEqual(res_2, 100)

	def test_negative_case(self):
		area_res = square.area(-1)
		per_res = square.perimeter(-1)
		self.assertEqual(area_res, 0)
		self.assertEqual(per_res, 0)

class TriangleTestCase(unittest.TestCase):
	def test_zero_case(self):
		area_zero_a_res = triangle.area(0, 5)
		area_zero_h_res = triangle.area(5, 0)
		per_zero_a_res = triangle.perimeter(0, 5, 6)
		per_zero_b_res = triangle.perimeter(5, 0, 6)
		per_zero_c_res = triangle.perimeter(5, 6, 0)
		self.assertEqual(area_zero_a_res, 0)
		self.assertEqual(area_zero_h_res, 0)
		self.assertEqual(per_zero_a_res, 0)
		self.assertEqual(per_zero_b_res, 0)
		self.assertEqual(per_zero_c_res, 0)

	def test_triangle_area(self):
		res_1 = triangle.area(5, 3)
		res_2 = triangle.area(8, 5)
		self.assertEqual(res_1, 7.5)
		self.assertEqual(res_2, 20)

	def test_triangle_perimeter(self):
		res_1 = triangle.perimeter(4, 7 ,9)
		res_2 = triangle.perimeter(3, 4, 5)
		self.assertEqual(res_1, 20)
		self.assertEqual(res_2, 12)

	def test_petimeter_of_impossible_tringle(self):
		res_1 = triangle.perimeter(1, 10, 15)
		res_2 = triangle.perimeter(10, 15, 1)
		res_3 = triangle.perimeter(15, 10, 1)
		self.assertEqual(res_1, 0)
		self.assertEqual(res_2, 0)
		self.assertEqual(res_3, 0)

	def test_negative_case(self):
		area_negative_a_res = triangle.area(-1, 5)
		area_negative_h_res = triangle.area(5, -1)
		per_negative_a_res = triangle.perimeter(-1, 5, 6)
		per_negative_b_res = triangle.perimeter(5, -1, 6)
		per_negative_c_res = triangle.perimeter(5, 6, -1)
		self.assertEqual(area_negative_a_res, 0)
		self.assertEqual(area_negative_h_res, 0)
		self.assertEqual(per_negative_a_res, 0)
		self.assertEqual(per_negative_b_res, 0)
		self.assertEqual(per_negative_c_res, 0)