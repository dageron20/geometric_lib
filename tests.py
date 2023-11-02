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
            ((0, 0), 0),
						((5, 0), 0),
            ((0, 'a'), KeyError),
            ((3, -3), KeyError),
            ((5, 5), 25),
        )
        self.perimeter_testcases = (
            ((0, 0), 0),
            ((5, 'a'), KeyError),
            ((-10, 0), KeyError),
            ((0, 10), 20),
            ((10, -10), KeyError),
        )

class SquareTest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        self.module = square
        self.area_testcases = (
            ((10, ), 100),
            (('a', ), KeyError),
            ((-1, ), KeyError),
            ((1.5, ), 2.25),
            ((12, ), 144),
        )
        self.perimeter_testcases = (
            ((0, ), 0),
            ((1, ), 4),
            ((-2, ), KeyError),
            ((100, ), 400),
            ((15, ), 60),
        )

class TriangleTest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        self.module = triangle
        self.area_testcases = (
            ((0, 123), 0),
            ((0, 2), 0),
            ((5, 0), 0),
            ((999999999999, 0), 0),
            ((5, -3), KeyError),
        )
        self.perimeter_testcases = (
            ((0, 0, 0), 0),
            ((0, 0, 1), KeyError),
            ((0, 1, 0), KeyError),
            ((1, 0, 0), KeyError),
            ((1, 0, -1), KeyError)
        )

class CircleTest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        self.module = circle
        self.area_testcases = (
            ((0, ), 0),
            ((1, ), math.pi),
            ((2, ), math.pi * 4),
            ((0.5, ), math.pi * 0.25),
        )
        self.perimeter_testcases = (
            ((0, ), 0),
            ((1, ), math.pi * 2),
            ((2, ), math.pi * 4),
            ((3, ), math.pi * 6),
            ((10, ), math.pi * 20),
            ((100, ), math.pi * 200),
            ((0.5, ), math.pi),
            ((1.3, ), math.pi * 2.6),
        )