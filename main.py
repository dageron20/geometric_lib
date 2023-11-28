import rectangle
import unittest
import circle
import square
import triangle

#Test-cases for rectangle
class RectangleTestCase(unittest.TestCase):
   
    def test_normal_area(self):
       res = rectangle.area(0.7, 10)
       self.assertEqual(res, 7)
       
    def test_normal_perimeter(self):
       res = rectangle.perimeter(10, 10)
       self.assertEqual(res, 40)
   
    def test_negative_area(self):
       res = rectangle.area(10, -1)
       self.assertEqual(res, "Negative arguments")
       
    def test_negative_perimeter(self):
       res = rectangle.perimeter(10, -1)
       self.assertEqual(res, "Negative arguments")

    def test_area_char(self):
       res = rectangle.area('c', 3)
       self.assertEqual(res, "Non-integer arguments")
       
    def test_perimeter_char(self):
       res = rectangle.perimeter('c', 5)
       self.assertEqual(res, "Non-integer arguments")

#Test-cases for circle
class CircleTestCase(unittest.TestCase):
   
    def test_area_normal(self):
       res = circle.area(10)
       self.assertEqual(res, 314.15926535897932384626433832795)
       
    def test_perimeter_normal(self):
       res = circle.perimeter(10)
       self.assertEqual(res, 62.83185307179586476925286766559)

    def test_negative_area(self):
       res = circle.area(-1)
       self.assertEqual(res, "Negative arguments")
       
    def test_negative_perimeter(self):
       res = circle.perimeter(-1)
       self.assertEqual(res, "Negative arguments")

    def test_area_char(self):
       res = circle.area('c')
       self.assertEqual(res, "Non-integer arguments")
       
    def test_perimeter_char(self):
       res = circle.perimeter('c')
       self.assertEqual(res, "Non-integer arguments")

#Test-cases for triangle
class TriangleTestCase(unittest.TestCase):
   
    def test_area_normal(self):
       res = triangle.area(5, 4)
       self.assertEqual(res, 10)
       
    def test_perimeter_normal(self):
       res = triangle.perimeter(10, 10, 5)
       self.assertEqual(res, 25)

    def test_negative_area(self):
       res = triangle.area(-8, 5)
       self.assertEqual(res, "Negative arguments")
       
    def test_negative_perimeter(self):
       res = triangle.perimeter(10, -1, 7)
       self.assertEqual(res, "Negative arguments")

    def test_area_char(self):
       res = triangle.area('c', 2)
       self.assertEqual(res, "Non-integer arguments")
       
    def test_perimeter_char(self):
       res = triangle.perimeter('c', 2, 3)
       self.assertEqual(res, "Non-integer arguments")

#Test-cases for square
class SquareTestCase(unittest.TestCase):
   
    def test_area_normal(self):
       res = square.area(10)
       self.assertEqual(res, 100)
       
    def test_perimeter_normal(self):
       res = square.perimeter(10)
       self.assertEqual(res, 40)

    def test_area_negative(self):
       res = square.area(-10)
       self.assertEqual(res, "Negative arguments")
       
    def test_perimeter_negative(self):
       res = square.perimeter(-3)
       self.assertEqual(res, "Negative arguments")

    def test_area_char(self):
       res = square.area('c')
       self.assertEqual(res, "Non-integer arguments")
       
    def test_perimeter_char(self):
       res = square.perimeter('c')
       self.assertEqual(res, "Non-integer arguments")


if __name__ == '__main__':
    unittest.main()
