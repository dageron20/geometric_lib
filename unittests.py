import unittest
import math

import rectangle
import square
import triangle
import circle


class BaseFigureTest(object):
    def test_area(self):
        try:
            self.area_testcases
        except:
            return
        for inp, outp in self.area_testcases:
            result = self.module.area(*inp)
            self.assertEqual(
                result,
                outp,
                f'{self.module.__name__}:area\t{inp=} returned={result}'
            )

    def test_perimeter(self):
        try:
            self.perimeter_testcases
        except:
            return
        for inp, outp in self.perimeter_testcases:
            result = self.module.perimeter(*inp)
            self.assertEqual(
                result,
                outp,
                f'{self.module.__name__}:perimeter\t{inp=}  returned={result}'
            )




class RectangleTest(unittest.TestCase, BaseFigureTest):
    def setUp(self):
        self.module = rectangle
        self.area_testcases = (
            ((1123, 0), 0),
            ((0, 0), 0),
            ((0, 1153), 0),
            ((100, 100), 10000),
            ((12, 13), 156),
            ((100, 1), 100),
            ((5, 5), 25),
            ((9, 10), 90),
            ((811, 3), 2433),
            ((1, 100), 100),
            ((0.9, 0.9), 0.9 * 0.9),
            ((0.04, 0.04), 0.04 * 0.04),
            ((1000000, 1000000), 1000000000000),
        )
        self.perimeter_testcases = (
            ((0, 0), 0),
            ((0, 4), 8),
            ((90, 0), 180),
            ((0, 10), 20),
            ((25, 25), 100),
            ((20, 20), 80),
            ((11, 13), 48),
            ((40, 20), 120),
            ((22, 9), 62),
            ((75, 50), 250),
            ((1, 2), 6),
            ((0.1, 0.2), (0.1 + 0.2) * 2),
            ((0.01, 0.02), 0.06),
        )


class SquareTest(unittest.TestCase, BaseFigureTest):
    def setUp(self):
        self.module = square
        self.area_testcases = (
            ((12,), 144),
            ((0,), 0),
            ((1,), 1),
            ((9,), 81),
            ((100,), 10000),
        )
        self.perimeter_testcases = (
            ((0,), 0),
            ((2,), 8),
            ((200,), 800),
            ((100,), 400),
            ((25,), 100),
            ((4,), 16),
            ((0.2,), 0.8),
            ((0.03,), 0.12),

        )


class TriangleTest(unittest.TestCase, BaseFigureTest):
    def setUp(self):
        self.module = triangle
        self.area_testcases = (
            ((0, 0), 0),
            ((1, 0), 0),
            ((0, 2), 0),
            ((100, 0), 0),
            ((6, 3), 9),
            ((2, 9), 9),
            ((100, 100), 500),
            ((30, 40), 600),
            ((0.5, 0.5), 0.125),
        )
        self.perimeter_testcases = (
            ((0, 0, 0), 0),
            ((0, 0, 5), 5),
            ((0, 5, 0), 5),
            ((5, 0, 0), 5),
            ((43, 24, 4), 71),
            ((6, 3, 65), 74),
            ((76, 30, 300), 406),
            ((213, 123, 321), 657),
            ((0.4, 0.5, 0.3), 1.2),

        )



class CircleTest(unittest.TestCase, BaseFigureTest):
    def setUp(self):
        self.module = circle
        self.area_testcases = (
            ((0,), 0),
            ((1,), math.pi),
            ((6,), math.pi * 36),
            ((7,), math.pi * 49),
            ((10,), math.pi * 100),
            ((20,), math.pi * 400),
            ((0.9,), math.pi * 0.81),
            ((1.5,), math.pi * 2.25),
        )
        self.perimeter_testcases = (
            ((0,), 0),
            ((1,), math.pi * 2),
            ((4,), math.pi * 8),
            ((9,), math.pi * 18),
            ((40,), math.pi * 80),
            ((100,), math.pi * 200),
            ((1.5,), math.pi * 3),
        )
