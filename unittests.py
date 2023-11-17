import unittest

import circle
import rectangle
import square
import triangle

class Figures_tests(unittest.TestCase):
   
    def test_circle_perimeter(self):
       res = circle.perimeter(0)
       self.assertEqual(res, "Figure isn't circle")
       res = circle.perimeter(10)
       self.assertEqual(res, 62.83185307179586)
       res = circle.perimeter(True)
       self.assertEqual(res, "Invalid input")
       res = circle.perimeter(-28)
       self.assertEqual(res, "Invalid input")

    def test_rectangle_perimeter(self): 
       res = rectangle.perimeter(15, 0)
       self.assertEqual(res, "Figure isn't rectangle")
       res = rectangle.perimeter("abcd", 12)
       self.assertEqual(res, "Invalid input")
       res = rectangle.perimeter(14, 13)
       self.assertEqual(res, 54)
       res = rectangle.perimeter(12, True)
       self.assertEqual(res, "Invalid input")
       res = rectangle.perimeter(23, -34)
       self.assertEqual(res, "Invalid input")

    def test_square_perimeter(self):
       res = square.perimeter(0)
       self.assertEqual(res, "Figure isn't square")
       res = square.perimeter("abcd")
       self.assertEqual(res, "Invalid input")
       res = square.perimeter(16)
       self.assertEqual(res, 64)
       res = square.perimeter(True)
       self.assertEqual(res, "Invalid input")
       res = square.perimeter(-34)
       self.assertEqual(res, "Invalid input")

    def test_triangle_perimeter(self):
       res = triangle.perimeter(15, 0, 10)
       self.assertEqual(res, "Figure isn't triangle")
       res = triangle.perimeter("abcd", 12, 23)
       self.assertEqual(res, "Invalid input")
       res = triangle.perimeter(14, 13, 11)
       self.assertEqual(res, 38)
       res = triangle.perimeter(12, True, 10)
       self.assertEqual(res, "Invalid input")
       res = triangle.perimeter(23, -34,  17)
       self.assertEqual(res, "Invalid input")
       res = triangle.perimeter(3, -3,  10)
       self.assertEqual(res, "The triangle inequality does't hold")


if __name__ == '__main__':
   unittest.main()