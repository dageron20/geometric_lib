import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import math
import circle
import rectangle
import square
import triangle
import unittest
class RectangleTestCase(unittest.TestCase):
    #area test
    def test_area_int(self):
        res = rectangle.area(125, 56)
        self.assertEqual(res, 7000)
    def test_zero_area(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_rectangle_area_double(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)
    def test_rectangle_area_big_data(self):
        res = rectangle.area(347889382374, 8380983389992)
        self.assertEqual(res, 2915655135231069652801008)

    def test_rectangle_area_fraction(self):
        res = rectangle.area(45.678, 21.5678)
        self.assertEqual(res, 985.1739683999998)

    # perimetr test
    def test_perimetr_int(self):
        res = rectangle.perimeter(28, 18)
        self.assertEqual(res, 92)
    def test_zero_perimetr(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_rectangle_perimetr_double(self):
        res = rectangle.perimeter(45, 45)
        self.assertEqual(res, 180)
    def test_rectangle_perimetr_big_data(self):
        res = rectangle.perimeter(347889382374, 8380983389992)
        self.assertEqual(res, 17457745544732)

    def test_rectangle_perimetr_fraction(self):
        res = rectangle.perimeter(789.123, 11.146)
        self.assertEqual(res, 1600.538)

class Circle_TestCase(unittest.TestCase):
    #area test
    def test_area_int(self):
        res = circle.area(425)
        self.assertEqual(res, 567450.1730546564)
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_circle_area_pi(self):
        res = circle.area(math.pi)
        self.assertEqual(res, 31.006276680299816)
    def test_area_big_data(self):
        res = circle.area(347889382374)
        self.assertEqual(res, 3.802176043589256e+23)

    def test_area_fraction(self):
        res = circle.area(56.234)
        self.assertEqual(res, 9934.541442970212)

    # perimetr test
    def test_perimetr_int(self):
        res = circle.perimeter(28)
        self.assertEqual(res, 175.92918860102841)
    def test_zero_perimetr(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_perimetr_pi(self):
        res = circle.perimeter(math.pi)
        self.assertEqual(res, 19.739208802178716)
    def test_perimetr_big_data(self):
        res = circle.perimeter(57512357891)
        self.assertEqual(res, 361360802081.9851)

    def test_perimetr_fraction(self):
        res = circle.perimeter(67.89732)
        self.assertEqual(res, 426.6114434208706)

class Square_TestCase(unittest.TestCase):
    #area test
    def test_area_int(self):
        res = square.area(789)
        self.assertEqual(res, 622521)
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_square_area_one(self):
        res = square.area(1)
        self.assertEqual(res, 1)
    def test_square_area_big_data(self):
        res = square.area(77634100891)
        self.assertEqual(res, 6027053621153966993881)

    def test_square_area_fraction(self):
        res = square.area(4567.3421)
        self.assertEqual(res, 20860613.85843241)

    # perimetr test
    def test_perimetr_int(self):
        res = square.perimeter(91)
        self.assertEqual(res, 364)
    def test_zero_perimetr(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_square_perimetr_one(self):
        res = square.perimeter(1)
        self.assertEqual(res, 4)
    def test_square_perimetr_big_data(self):
        res = square.perimeter(457997155624564456)
        self.assertEqual(res, 1831988622498257824)

    def test_square_perimetr_fraction(self):
        res = square.perimeter(443.67865)
        self.assertEqual(res, 1774.7146)

class Triangle_TestCase(unittest.TestCase):
    #area test
    def test_area_int(self):
        res = triangle.area(3216, 349)
        self.assertEqual(res, 561192.0)
    def test_zero_side_area(self):
        res = triangle.area(0, 5)
        self.assertEqual(res, 0)

    def test_zero_height_area(self):
        res = triangle.area(5, 0)
        self.assertEqual(res, 0)
    def test_triangle_area_big_data(self):
        res = triangle.area(9423847329131, 84823929121)
        self.assertEqual(res, 3.9968387894666656e+23)

    def test_triangle_area_fraction(self):
        res = triangle.area(2439.999, 14.3136)
        self.assertEqual(res, 17462.5848432)

    # perimetr test
    def test_perimetr_int(self):
        res = triangle.perimeter(63, 56, 89)
        self.assertEqual(res, 208)
    def test_zero_perimetr(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_zero_one_side_perimetr(self):
        res = triangle.perimeter(0, 4, 8)
        self.assertEqual(res, 12)
    def test_triangle_perimetr_big_data(self):
        res = triangle.perimeter(46544561578, 32690642383, 5785126333457)
        self.assertEqual(res, 5864361537418)

    def test_square_perimetr_fraction(self):
        res = triangle.perimeter(67.8963, 320.124005, 1221.511889)
        self.assertEqual(res, 1609.5321940000001)