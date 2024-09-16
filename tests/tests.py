import unittest

import bin.circle
import bin.rectangle
import bin.square
import bin.triangle


class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        area_result = bin.circle.area(0)
        self.assertEqual(area_result, 0)

        perimeter_result = bin.circle.perimeter(0)
        self.assertEqual(perimeter_result, 0)

    def test_area(self):
        result_1 = bin.circle.area(3)
        self.assertEqual(result_1, 28.274333882308138)

        result_2 = bin.circle.area(100)
        self.assertEqual(result_2, 31415.926535897932)

        result_3 = bin.circle.area(25.6)
        self.assertEqual(result_3, 2058.874161456607)

        result_4 = bin.circle.area(0.51)
        self.assertEqual(result_4, 0.8171282491987052)

        result_5 = bin.circle.area(9492349)
        self.assertEqual(result_5, 283072230705944.7)

    def test_perimeter(self):
        result_1 = bin.circle.perimeter(15)
        self.assertEqual(result_1, 94.24777960769379)

        result_2 = bin.circle.perimeter(191)
        self.assertEqual(result_2, 1200.088393671301)

        result_3 = bin.circle.perimeter(14.2)
        self.assertEqual(result_3, 89.22123136195012)

        result_4 = bin.circle.perimeter(0.96)
        self.assertEqual(result_4, 6.031857894892402)

        result_5 = bin.circle.perimeter(1941914)
        self.assertEqual(result_5, 12201405.51260634)


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        area_result_1 = bin.rectangle.area(0, 5)
        self.assertEqual(area_result_1, 0)

        area_result_2 = bin.rectangle.area(6, 0)
        self.assertEqual(area_result_2, 0)

    def test_square_mul(self):
        area_result = bin.rectangle.area(5, 5)
        self.assertEqual(area_result, 25)

        perimeter_result = bin.rectangle.perimeter(4, 12)
        self.assertEqual(perimeter_result, 32)

    def test_area(self):
        result_1 = bin.rectangle.area(3, 5)
        self.assertEqual(result_1, 15)

        result_2 = bin.rectangle.area(100, 1)
        self.assertEqual(result_2, 100)

        result_3 = bin.rectangle.area(491941, 9349394)
        self.assertEqual(result_3, 4599350233754)

        result_4 = bin.rectangle.area(0.77, 0.26)
        self.assertEqual(result_4, 0.20020000000000002)

        result_5 = bin.rectangle.area(1414.22, 199.942)
        self.assertEqual(result_5, 282761.97524)

    def test_perimeter(self):
        result_1 = bin.rectangle.perimeter(12, 22)
        self.assertEqual(result_1, 68)

        result_2 = bin.rectangle.perimeter(920, 195)
        self.assertEqual(result_2, 2230)

        result_3 = bin.rectangle.perimeter(38.3, 19.1)
        self.assertEqual(result_3, 114.8)

        result_4 = bin.rectangle.perimeter(0.524, 0.444)
        self.assertEqual(result_4, 1.936)

        result_5 = bin.rectangle.perimeter(84184841, 6461611)
        self.assertEqual(result_5, 181292904)


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        area_result = bin.square.area(0)
        self.assertEqual(area_result, 0)

        perimeter_result = bin.square.perimeter(0)
        self.assertEqual(perimeter_result, 0)

    def test_area(self):
        result_1 = bin.square.area(4)
        self.assertEqual(result_1, 16)

        result_2 = bin.square.area(50)
        self.assertEqual(result_2, 2500)

        result_3 = bin.square.area(42.1)
        self.assertEqual(result_3, 1772.41)

        result_4 = bin.square.area(0.22)
        self.assertEqual(result_4, 0.0484)

        result_5 = bin.square.area(22222222)
        self.assertEqual(result_5, 493827150617284)

    def test_perimeter(self):
        result_1 = bin.square.perimeter(7)
        self.assertEqual(result_1, 28)

        result_2 = bin.square.perimeter(101)
        self.assertEqual(result_2, 404)

        result_3 = bin.square.perimeter(57.7)
        self.assertEqual(result_3, 230.8)

        result_4 = bin.square.perimeter(0.13)
        self.assertEqual(result_4, 0.52)

        result_5 = bin.square.perimeter(99999999)
        self.assertEqual(result_5, 399999996)


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        area_result_1 = bin.triangle.area(0, 55)
        self.assertEqual(area_result_1, 0)

        area_result_2 = bin.triangle.area(44, 0)
        self.assertEqual(area_result_2, 0)

    def test_area(self):
        result_1 = bin.triangle.area(4, 2)
        self.assertEqual(result_1, 4)

        result_2 = bin.triangle.area(102, 1)
        self.assertEqual(result_2, 51)

        result_3 = bin.triangle.area(4414121, 232323)
        self.assertEqual(result_3, 512750916541.5)

        result_4 = bin.triangle.area(0.55, 0.66)
        self.assertEqual(result_4, 0.18150000000000002)

        result_5 = bin.triangle.area(4154.22, 881.323)
        self.assertEqual(result_5, 1830604.81653)

    def test_perimeter(self):
        result_1 = bin.triangle.perimeter(10, 20, 30)
        self.assertEqual(result_1, 60)

        result_2 = bin.triangle.perimeter(414, 252, 676)
        self.assertEqual(result_2, 1342)

        result_3 = bin.triangle.perimeter(31.2, 52.2, 34.5)
        self.assertEqual(result_3, 117.9)

        result_4 = bin.triangle.perimeter(0.111, 0.444, 0.777)
        self.assertEqual(result_4, 1.332)

        result_5 = bin.triangle.perimeter(481284128, 21323131, 10100011)
        self.assertEqual(result_5, 512707270)