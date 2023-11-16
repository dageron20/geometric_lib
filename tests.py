import unittest
import math

import rectangle
import square
import triangle
import circle

class BaseTestCase(object):
    def test_perimeter(self):
        for inp, outp in self.perimeter_testcases:
            result = self.module.perimeter(*inp)
            self.assertEqual(result, outp, f'{self.module.__name__}:perimeter\t{inp=} expected={outp} returned={result}')
            
    def test_area(self):
        for inp, outp in self.area_testcases:
            result = self.module.area(*inp)
            self.assertEqual(result, outp, f'{self.module.__name__}:area\t{inp=} expected={outp} returned={result}')
            
    
class RectangleTest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        self.module = rectangle
        self.area_testcases = (
            ((3, 2), 6),
            ((3.2, 2), 6.4),
						((5, 0), KeyError),
            ((6, 'a'), KeyError),
            ((3, -3), KeyError),
            ((5, True), KeyError),
        )
        self.perimeter_testcases = (
            ((3, 2), 10),
            ((3.2, 2), 10.4),
						((5, 0), KeyError),
            ((6, 'a'), KeyError),
            ((3, -3), KeyError),
            ((5, True), KeyError),
        )

class SquareTest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        self.module = square
        self.area_testcases = (
            ((3), 9),
            ((0.5), 0.25),
						((0), KeyError),
            (('a'), KeyError),
            ((-3), KeyError),
            ((5, True), KeyError),
        )
        self.perimeter_testcases = (
            ((3), 12),
            ((0.5), 2),
						((0), KeyError),
            (('a'), KeyError),
            ((-3), KeyError),
            ((True), KeyError),
        )

class TriangleTest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        self.module = triangle
        self.area_testcases = (
            ((0, 0, ), KeyError),
            ((6, 8,), 24),
            ((6, 0.5), 1.5),
            ((0, -1), KeyError),
            ((1, True), KeyError),
            ((1, 'g'), KeyError)
        )
        self.perimeter_testcases = (
            ((0, 0, 0), KeyError),
            ((6, 8, 10), 24),
            ((6, 8.2, 10), 24.2),
            ((0, -1, 0), KeyError),
            ((1, True, 0), KeyError),
            ((1, 'g', -1), KeyError)
        )

class CircleTest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        self.module = circle
        self.area_testcases = (
            ((0, ), KeyError),
            ((1, ), math.pi),
            (('a', ), KeyError),
            ((0.5, ), math.pi * 0.25),
            ((True), KeyError),
            ((-1), KeyError)
        )
        self.perimeter_testcases = (
            ((0, ), KeyError),
            ((1, ), math.pi * 2),
            ((-1, ), KeyError),
            ((True, ), KeyError),
            (("a", ), KeyError),
            ((1.3, ), math.pi * 2.6),
        )