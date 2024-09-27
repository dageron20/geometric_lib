import unittest
import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):

    def test_zero_mul(self):
        result = circle.area(0)
        self.assertEqual(result, 0)

    def test_area(self):
        result_1 = circle.area(5)
        self.assertEqual(result_1, 78.53981633974483)

        result_2 = circle.area(10)
        self.assertEqual(result_2, 314.1592653589793)

        result_3 = circle.area(15)
        self.assertEqual(result_3, 706.8583470577034)
    
    def test_perimeter(self):
        result_1 = circle.perimeter(5)
        self.assertEqual(result_1, 31.41592653589793)

        result_2 = circle.perimeter(10)
        self.assertEqual(result_2, 62.83185307179586)

        result_3 = circle.perimeter(15)
        self.assertEqual(result_3, 94.24777960769379)
    
class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        result_1 = rectangle.area(0, 2)
        self.assertEqual(result_1, 0)

        result_2 = rectangle.area(5, 0)
        self.assertEqual(result_2, 0)

    def test_square_mul(self):
        result = rectangle.area(10, 10)
        self.assertEqual(result, 100)

    def test_area(self):
        result_1 = rectangle.area(6, 2)
        self.assertEqual(result_1, 12)

        result_2 = rectangle.area(4, 500)
        self.assertEqual(result_2, 2000)

        result_3 = rectangle.area(123, 456)
        self.assertEqual(result_3, 56088)

        result_4 = rectangle.area(1.5, 1.9)
        self.assertEqual(result_4, 2.8499999999999996)

    def test_perimeter(self):
        result_1 = rectangle.perimeter(12, 56)
        self.assertEqual(result_1, 136)

        result_2 = rectangle.perimeter(456, 78)
        self.assertEqual(result_2, 1068)

        result_3 = rectangle.perimeter(45.4, 34.96)
        self.assertEqual(result_3, 160.72)

        result_4 = rectangle.perimeter(0.4, 3464)
        self.assertEqual(result_4, 6928.8)


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        result_1 = square.area(0)
        self.assertEqual(result_1, 0)

        result_2 = square.perimeter(0)
        self.assertEqual(result_2, 0)

    def test_area(self):
        result_1 = square.area(8)
        self.assertEqual(result_1, 64)

        result_2 = square.area(657)
        self.assertEqual(result_2, 431649)

        result_3 = square.area(87.62)
        self.assertEqual(result_3, 7677.264400000001)

        result_4 = square.area(45650.1)
        self.assertEqual(result_4, 2083931630.0099998)

    def test_perimeter(self):
        result_1 = square.perimeter(4)
        self.assertEqual(result_1, 16)

        result_2 = square.perimeter(85)
        self.assertEqual(result_2, 340)

        result_3 = square.perimeter(786.76)
        self.assertEqual(result_3, 3147.04)

        result_4 = square.perimeter(6.785)
        self.assertEqual(result_4, 27.14)


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        result_1 = triangle.area(0, 3)
        self.assertEqual(result_1, 0)

        result_2 = triangle.area(3, 0)
        self.assertEqual(result_2, 0)

    def test_area(self):
        result_1 = triangle.area(4, 9)
        self.assertEqual(result_1, 18)

        result_2 = triangle.area(285, 9)
        self.assertEqual(result_2, 1282.5)

        result_3 = triangle.area(2.165, 8.9)
        self.assertEqual(result_3, 9.63425)

        result_4 = triangle.area(11.04, 0.8)
        self.assertEqual(result_4, 4.4159999999999995)

    def test_perimeter(self):
        result_1 = triangle.perimeter(34, 7, 3)
        self.assertEqual(result_1, 44)

        result_2 = triangle.perimeter(647, 766, 2399)
        self.assertEqual(result_2, 3812)

        result_3 = triangle.perimeter(314.14, 324.4, 7867.777)
        self.assertEqual(result_3, 8506.317)

        result_4 = triangle.perimeter(7648, 768.68, 0.45235)
        self.assertEqual(result_4, 8417.13235)