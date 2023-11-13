import unittest
import circle
import rectangle
import square
import triangle

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(circle.area(0), 0)
        self.assertEqual(circle.perimeter(0), 0)

    def test_single_digit_number_mul(self):
        self.assertEqual(circle.area(2), 12.566370614359172)
        self.assertEqual(circle.perimeter(3), 18.84955592153876)

    def test_multi_digit_number_mul(self):
        self.assertEqual(circle.area(235), 173494.45429449633)
        self.assertEqual(circle.perimeter(343), 2155.1325603625983)

    def test_string(self):
        self.assertEqual(circle.area("11"), 380.1327110843649)
        self.assertEqual(circle.perimeter("11"), 69.11503837897544)

    def test_negative_num(self):
        self.assertEqual(circle.area(-472), 0)
        self.assertEqual(circle.perimeter(-472), 0)

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(rectangle.area(10, 0), 0)
        self.assertEqual(rectangle.perimeter(10, 0), 0)
    
    def test_square_mul(self):
        self.assertEqual(rectangle.area(10, 10), 100)
        self.assertEqual(rectangle.perimeter(10, 10), 40)

    def test_arbitrary_numbers_mul(self):
        self.assertEqual(rectangle.area(9, 21), 189)
        self.assertEqual(rectangle.perimeter(33, 7), 80)

    def test_string(self):
        self.assertEqual(rectangle.area("37", "13"), 481)
        self.assertEqual(rectangle.perimeter("37", "13"), 100)

    def test_negative_num(self):
        self.assertEqual(rectangle.area(-3, 5), 0)
        self.assertEqual(rectangle.perimeter(36, -10), 0)

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.perimeter(0), 0)

    def test_single_digit_number_mul(self):
        self.assertEqual(square.area(5), 25)
        self.assertEqual(square.perimeter(9), 36)

    def test_multi_digit_number_mul(self):
        self.assertEqual(square.area(11), 121)
        self.assertEqual(square.perimeter(363), 1452)

    def test_string(self):
        self.assertEqual(square.area("245"), 60025)
        self.assertEqual(square.perimeter("245"), 980)

    def test_negative_num(self):
        self.assertEqual(square.area(-25), 0)
        self.assertEqual(square.perimeter(-67), 0)

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(triangle.area(0, 5), 0)
        self.assertEqual(triangle.perimeter(10, 0, 1), 0)

    def test_single_digit_number_mul(self):
        self.assertEqual(triangle.area(9, 5), 22.5)
        self.assertEqual(triangle.perimeter(3, 1, 9), 13)

    def test_multi_digit_number_mul(self):
        self.assertEqual(triangle.area(45, 137), 3082.5)
        self.assertEqual(triangle.perimeter(346, 121, 5890), 6357)

    def test_string(self):
        self.assertEqual(triangle.area("34", "23"), 391)
        self.assertEqual(triangle.perimeter("35", "23", "11"), 69)

    def test_negative_num(self):
        self.assertEqual(triangle.area(-67, 41), 0)
        self.assertEqual(triangle.perimeter(-2, 190, -56), 0)