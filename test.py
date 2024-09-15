import unittest
import math
import circle
import square
import triangle
import rectangle

'''
Проверяется все возможные случаи при вычеслении площади и периметра:
когда все параметры >0;
когда хотя-бы 1 из параметров =0;
когда хотя-бы 1 из параметров <0;
'''
 
class RectangleTestCase(unittest.TestCase):
   def test_zero_mul_1(self):
       res = rectangle.area(10, 0)
       self.assertEqual(res, "wrong parameter(s)")

   def test_zero_mul_2(self):
       res = rectangle.area(0, 10)
       self.assertEqual(res, "wrong parameter(s)")

   def test_double_zero_mul(self):
       res = rectangle.area(0, 0)
       self.assertEqual(res, "wrong parameter(s)")
       
   def test_square_mul(self):
       res = rectangle.area(10, 10)
       self.assertEqual(res, 100)

   def test_dif_mul_1(self):
       res = rectangle.area(23, 10)
       self.assertEqual(res, 230)
    
   def test_negative_mul_1(self):
       res = rectangle.area(10, -6)
       self.assertEqual(res, "wrong parameter(s)")

   def test_negative_mul_2(self):
       res = rectangle.area(-6, 10)
       self.assertEqual(res, "wrong parameter(s)")

   def test_double_negative_mul(self):
       res = rectangle.area(-6, -5)
       self.assertEqual(res, "wrong parameter(s)")
    
   def test_zero_per_1(self):
       res = rectangle.perimeter(0, 10)
       self.assertEqual(res, "wrong parameter(s)")

   def test_zero_per_2(self):
       res = rectangle.perimeter(10, 0)
       self.assertEqual(res, "wrong parameter(s)")

   def test_double_zero_per(self):
       res = rectangle.perimeter(0, 0)
       self.assertEqual(res, "wrong parameter(s)")

   def test_square_per(self):
       res = rectangle.perimeter(10, 10)
       self.assertEqual(res, 40)

   def test_dif_per(self):
       res = rectangle.perimeter(1, 10)
       self.assertEqual(res, 22)

   def test_negative_per_1(self):
       res = rectangle.perimeter(10, -6)
       self.assertEqual(res, "wrong parameter(s)")

   def test_negative_per_2(self):
       res = rectangle.perimeter(-6, 10)
       self.assertEqual(res, "wrong parameter(s)")

   def test_double_negative_per(self):
       res = rectangle.perimeter(-6, -5)
       self.assertEqual(res, "wrong parameter(s)")

class TriangleTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = triangle.area(10, 0)
       self.assertEqual(res, "wrong parameter(s)")

   def test_zero_mul_1(self):
       res = triangle.area(0, 10)
       self.assertEqual(res, "wrong parameter(s)")

   def test_zero_mul_2(self):
       res = triangle.area(0, 0)
       self.assertEqual(res, "wrong parameter(s)")
       
   def test_square_mul(self):
       res = triangle.area(10, 10)
       self.assertEqual(res, 50)

   def test_dif_mul_1(self):
       res = triangle.area(23, 10)
       self.assertEqual(res, 115)
    
   def test_negative_mul_1(self):
       res = triangle.area(10, -6)
       self.assertEqual(res, "wrong parameter(s)")

   def test_negative_mul_2(self):
       res = triangle.area(-6, 10)
       self.assertEqual(res, "wrong parameter(s)")

   def test_double_negative_mul(self):
       res = triangle.area(-6, -5)
       self.assertEqual(res, "wrong parameter(s)")
    
   def test_zero_per_1(self):
       res = triangle.perimeter(0, 10, 10)
       self.assertEqual(res, "wrong parameter(s)")

   def test_zero_per_2(self):
       res = triangle.perimeter(10, 0, 10)
       self.assertEqual(res, "wrong parameter(s)")

   def test_zero_per_3(self):
       res = triangle.perimeter(10, 10, 0)
       self.assertEqual(res, "wrong parameter(s)")

   def test_double_zero_per_1(self):
       res = triangle.perimeter(0, 0, 10)
       self.assertEqual(res, "wrong parameter(s)")

   def test_double_zero_per_2(self):
       res = triangle.perimeter(0, 10, 0)
       self.assertEqual(res, "wrong parameter(s)")

   def test_double_zero_per_3(self):
       res = triangle.perimeter(10, 0, 0)
       self.assertEqual(res, "wrong parameter(s)")

   def test_triple_zero_per(self):
       res = triangle.perimeter(0, 0, 0)
       self.assertEqual(res, "wrong parameter(s)")

   def test_triple_per(self):
       res = triangle.perimeter(10, 10, 10)
       self.assertEqual(res, 30)

   def test_dif_per_1(self):
       res = triangle.perimeter(1, 10, 2)
       self.assertEqual(res, 13)

   def test_negative_per_1(self):
       res = triangle.perimeter(10, -6, 10)
       self.assertEqual(res, "wrong parameter(s)")

   def test_negative_per_2(self):
       res = triangle.perimeter(-6, 10, 10)
       self.assertEqual(res, "wrong parameter(s)")

   def test_double_negative_per(self):
       res = triangle.perimeter(-6, -5, 10)
       self.assertEqual(res, "wrong parameter(s)")

class SquareTestCase(unittest.TestCase):
   def test_zero_mul_1(self):
       res = square.area(0)
       self.assertEqual(res, "wrong parameter")
       
   def test_square_mul(self):
       res = square.area(10)
       self.assertEqual(res, 100)

   def test_negative_mul(self):
       res = square.area(-6)
       self.assertEqual(res, "wrong parameter")
    
   def test_zero_per_1(self):
       res = square.perimeter(0)
       self.assertEqual(res, "wrong parameter")

   def test_square_per(self):
       res = square.perimeter(10)
       self.assertEqual(res, 40)

   def test_negative_per(self):
       res = square.perimeter(-6)
       self.assertEqual(res, "wrong parameter")

class circleTestCase(unittest.TestCase):
   def test_zero_mul_1(self):
       res = circle.area(0)
       self.assertEqual(res, "wrong parameter")
       
   def test_circle_mul(self):
       res = circle.area(10)
       self.assertEqual(res, math.pi*100)

   def test_negative_mul(self):
       res = circle.area(-6)
       self.assertEqual(res, "wrong parameter")
    
   def test_zero_per_1(self):
       res = circle.perimeter(0)
       self.assertEqual(res, "wrong parameter")

   def test_circle_per(self):
       res = circle.perimeter(10)
       self.assertEqual(res, math.pi*20)

   def test_negative_per(self):
       res = circle.perimeter(-6)
       self.assertEqual(res, "wrong parameter")
       