import unittest

import circle
import square
import triangle
import rectangle
import math

class TriangleTests(unittest.TestCase):
    def test_perimeter_check(self):
        a, b, c = 7777777777777777777777777777, 6666666444444444444444442, 23333333333333333333333
        self.assertEqual(triangle.perimeter(a, b, c), a + b + c)
        self.assertEqual(triangle.perimeter(10, 20, 80), 110)

    def test_area_check(self):
        a, h = 3322222222222222222222222222222222222222, 10000000000000000000000000000000000000000000000000000000000000
        self.assertEqual(triangle.area(a, h), a * h / 2)
        self.assertEqual(triangle.area(4, 1000), 2000)



class RectangleTests(unittest.TestCase):

    def test_perimeter_check(self):
        a, b = 11111111111111111111111, 2333333333333333333333333
        self.assertEqual(rectangle.perimeter(a, b), (a + b) * 2)
        self.assertEqual(rectangle.perimeter(100, 100), 400)

    def test_area_check(self):
        self.assertEqual(rectangle.area(5, 8), 40)
        self.assertEqual(rectangle.area(9, 9), 81)



class CircleTests(unittest.TestCase):
    def test_perimeter_check(self):
        self.assertEqual(circle.perimeter(800), 2 * 800 * math.pi)
        self.assertEqual(circle.perimeter(777), 2 * 777 * math.pi)

    def test_area_check(self):
        self.assertEqual(circle.area(777) // 1, 777 * 777 * math.pi // 1)
        self.assertEqual(circle.area(99) // 1, 99 * 99 * math.pi // 1)

class SquareTests(unittest.TestCase):

    def test_perimeter_check(self):
        self.assertEqual(square.perimeter(10), 40)
        self.assertEqual(square.perimeter(200), 800)

    def test_area_check(self):
        self.assertEqual(square.area(10), 100)
        self.assertEqual(square.area(11), 121)



if __name__ == '__main__':
    unittest.main()
