import unittest
import circle
import rectangle
import square
import triangle

class CircleTestCase(unittest.TestCase):
    '''circle TestCase'''
    
    def test_circle_zero_area(self):
        self.assertEqual(circle.area(0), 0)

    def test_circle_positive_area(self):
        self.assertEqual(int(circle.area(23)), 1661)
        self.assertEqual(int(circle.area(150)), 70685)
        self.assertEqual(int(circle.area(1777)), 9920298)
    
    def test_circle_perimeter(self):
        self.assertEqual(circle.perimeter(0), 0)
        self.assertEqual(int(circle.perimeter(23)), 144)

class RectangleTestCase(unittest.TestCase):
    '''rectangle TestCase'''

    def test_rectangle_zero_area(self):
        self.assertEqual(rectangle.area(0, 0), 0)
        self.assertEqual(rectangle.area(5, 0), 0)
        self.assertEqual(rectangle.area(0, 5), 0)
    
    def test_rectangle_positive_area(self):
        self.assertEqual(rectangle.area(1, 1), 1)
        self.assertEqual(rectangle.area(23, 2), 46)
        self.assertEqual(rectangle.area(2, 100), 200)
        self.assertEqual(rectangle.area(223, 576), 128448)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)
        self.assertEqual(rectangle.perimeter(5, 5), 20)
        self.assertEqual(rectangle.perimeter(23, 12), 70)
        self.assertEqual(rectangle.perimeter(236, 867), 2206)

class SquareTestCase(unittest.TestCase):
    '''square TestCase'''

    def test_square_zero_area(self):
        self.assertEqual(square.area(0), 0)
    
    def test_square_positive_area(self):
        self.assertEqual(square.area(5), 25)
        self.assertEqual(square.area(23), 529)
        self.assertEqual(square.area(156), 24336)
        self.assertEqual(square.area(2422), 5866084)

    def test_square_perimeter(self):
        self.assertEqual(square.perimeter(0), 0)
        self.assertEqual(square.perimeter(5), 20)
        self.assertEqual(square.perimeter(23), 92)
        self.assertEqual(square.perimeter(156), 624)

class TriangleTestCase(unittest.TestCase):
    '''triangle TestCase'''

    def test_triangle_zero_area(self):
        self.assertEqual(triangle.area(0, 0), 0)
        self.assertEqual(triangle.area(5, 0), 0)
        self.assertEqual(triangle.area(0, 5), 0)

    def test_triangle_positive_area(self):
        self.assertEqual(triangle.area(5, 2), 5)
        self.assertEqual(triangle.area(7, 3), 10.5)
        self.assertEqual(triangle.area(123, 56), 3444)
        self.assertEqual(triangle.area(2135, 242), 258335)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)
        self.assertEqual(triangle.perimeter(2, 5, 8), 15)
        self.assertEqual(triangle.perimeter(23, 67, 98), 188)
        self.assertEqual(triangle.perimeter(2362, 3924, 8123), 14409)
