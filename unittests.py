import unittest
import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_circle_area(self):
        self.assertEqual(circle.area(1413), 6272406.50278512)
        self.assertEqual(circle.area(0.5), 0.7853981633974483)

    def test_circle_area_zero(self):
        self.assertEqual(circle.area(0), "input must be greater than zero")

    def test_circle_area_negative(self):
        self.assertEqual(circle.area(-1.5), "input must be greater than zero")

    def test_circle_area_character(self):
        self.assertEqual(circle.area("&"), "input can not contain characters")

    def test_circle_perimeter(self):
        self.assertEqual(circle.perimeter(1413), 8878.140839044756)
        self.assertEqual(circle.perimeter(0.5), 3.141592653589793)

    def test_circle_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), "input must be greater than zero")

    def test_circle_perimeter_negative(self):
        self.assertEqual(circle.perimeter(-1.5), "input must be greater than zero")

    def test_circle_perimeter_character(self):
        self.assertEqual(circle.perimeter("&"), "input can not contain characters")
class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle.area(1413, 796), 1124748)
        self.assertEqual(rectangle.area(0.5, 5), 2.5)

    def test_rectangle_area_zero(self):
        self.assertEqual(rectangle.area(0,5), "input must be greater than zero")

    def test_rectangle_area_negative(self):
        self.assertEqual(rectangle.area(-1.5,5), "input must be greater than zero")

    def test_rectangle_area_character(self):
        self.assertEqual(rectangle.area("&",5), "input can not contain characters")

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(1413,796), 4418)
        self.assertEqual(rectangle.perimeter(0.5,0.1), 1.2)

    def test_rectangle_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(0,5), "input must be greater than zero")

    def test_rectangle_perimeter_negative(self):
        self.assertEqual(rectangle.perimeter(-1.5,5), "input must be greater than zero")

    def test_rectangle_perimeter_character(self):
        self.assertEqual(rectangle.perimeter("&",5), "input can not contain characters")
class SquareTestCase(unittest.TestCase):
    def test_square_area(self):
        self.assertEqual(square.area(1413), 1996569)
        self.assertEqual(square.area(0.5), 0.25)

    def test_square_area_zero(self):
        self.assertEqual(square.area(0), "input must be greater than zero")

    def test_square_area_negative(self):
        self.assertEqual(square.area(-1.5), "input must be greater than zero")

    def test_square_area_character(self):
        self.assertEqual(square.area("&"), "input can not contain characters")

    def test_square_perimeter(self):
        self.assertEqual(square.perimeter(1413), 5652)
        self.assertEqual(square.perimeter(0.1), 0.4)

    def test_square_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), "input must be greater than zero")

    def test_square_perimeter_negative(self):
        self.assertEqual(square.perimeter(-1.5), "input must be greater than zero")

    def test_square_perimeter_character(self):
        self.assertEqual(square.perimeter("&"), "input can not contain characters")
class TriangleTestCase(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(triangle.area(1413,10), 7065)
        self.assertEqual(triangle.area(0.5,0.2), 0.05)

    def test_triangle_area_zero(self):
        self.assertEqual(triangle.area(0,128), "input must be greater than zero")

    def test_triangle_area_negative(self):
        self.assertEqual(triangle.area(-1.5,128), "input must be greater than zero")

    def test_triangle_area_character(self):
        self.assertEqual(triangle.area("&",128), "input can not contain characters")

    def test_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(1413,4573,1834), 7820)
        self.assertEqual(triangle.perimeter(0.1,0.5,0.4), 1)

    def test_triangle_perimeter_zero(self):
        self.assertEqual(triangle.perimeter(0,0,1), "input must be greater than zero")

    def test_triangle_perimeter_negative(self):
        self.assertEqual(triangle.perimeter(-1.5,5,4), "input must be greater than zero")

    def test_triangle_perimeter_character(self):
        self.assertEqual(triangle.perimeter("&","a",1), "input can not contain characters")

if __name__ == '__main__':
    unittest.main()
