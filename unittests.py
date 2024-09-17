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
        f'{self.module.__name__}:area\t{inp=} expected={outp} returned={result}'
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
        f'{self.module.__name__}:perimeter\t{inp=} expected={outp} returned={result}'
)

def test_exception(self):
try:
self.exception_testcases
        except:
return
for inp, func, expected in self.exception_testcases:
self.assertRaises(
        expected,
        func,
        *inp
)


class Pryamoyg(unittest.TestCase, BaseFigureTest):
def setUp(self):
self.module = rectangle
self.area_testcases = (
        ((3, 0), 0),
                ((0, 3), 0),
                ((0, 0), 0),
                ((20, 20), 400),
                ((5, 5), 25),
                ((100, 100), 10000),
                ((5, 3), 15),
                ((3, 5), 15),
                ((100, 1), 100),
                ((1, 100), 100),
                ((0.2, 0.2), 0.2 * 0.2),
                ((0.02, 0.02), 0.02 * 0.02),
                ((-1, -1), 1),
                ((1000000, 5000000), 5000000000000),
                ((-1, 5), -5),
                (('a', 5), 'aaaaa'),
                ((3, 'ab'), 'ababab'),
)
self.perimeter_testcases = (
        ((0, 0), 0),
                ((5, 4), 18),
                ((10, 0), 20),
                ((0, 10), 20),
                ((10, 10), 40),
                ((20, 20), 80),
                ((13, 13), 52),
                ((10, 20), 60),
                ((20, 10), 60),
                ((13, 12), 50),
                ((1, 2), 6),
                ((0.1, 0.2), (0.1 + 0.2) * 2),
                ((0.01, 0.02), 0.06),
)
self.exception_testcases = (
        (('a', 'a'), self.module.area, TypeError),
                ((dict(), 1), self.module.area, TypeError),
                (('a', 4), self.module.perimeter, TypeError),
)


class Kvadrat(unittest.TestCase, BaseFigureTest):
def setUp(self):
self.module = square
self.area_testcases = (
        ((10,), 100),
                ((0,), 0),
                ((1,), 1),
                ((2,), 4),
                ((70,), 4900),
)
self.perimeter_testcases = (
        ((0,), 0),
                ((1,), 4),
                ((2,), 8),
                ((100,), 400),
                ((15,), 60),
                ((3,), 12),
                ((0.1,), 0.4),
                ((0.01,), 0.04),
                (('a',), 'aaaa'),
)
self.exception_testcases = (
        (('a',), self.module.area, TypeError),
)


class Treyg(unittest.TestCase, BaseFigureTest):
def setUp(self):
self.module = triangle
self.area_testcases = (
        ((0, 1), 0),
                ((1, 0), 0),
                ((0, 100), 0),
                ((100, 0), 0),
                ((5, 3), 7.5),
                ((3, 3), 4.5),
                ((10, 10), 50),
                ((30, 70), 1050),
                ((0.5, 0.5), 0.125),
)
self.perimeter_testcases = (
        ((0, 0, 0), 0),
                ((0, 0, 1), 1),
                ((0, 1, 0), 1),
                ((1, 0, 0), 1),
                ((1, 2, 3), 6),
                ((3, 2, 1), 6),
                ((3, 3, 3), 9),
                ((100, 100, 100), 300),
                ((0.5, 0.5, 0.5), 1.5),
                (('a', 'b', 'c'), 'abc'),
                (('c', 'b', 'a'), 'cba'),
)
self.exception_testcases = (
        (('a', 'b'), self.module.area, TypeError),
                (('a', 1), self.module.area, TypeError),
                ((1, 'a'), self.module.area, TypeError),
                ((1, 'a', 'a'), self.module.perimeter, TypeError),
                (('a', 1, 'a'), self.module.perimeter, TypeError),
                (('a', 'a', 1), self.module.perimeter, TypeError),
)


class CircleTest(unittest.TestCase, BaseFigureTest):
def setUp(self):
self.module = circle
self.area_testcases = (
        ((0,), 0),
                ((1,), math.pi),
                ((2,), math.pi * 4),
                ((3,), math.pi * 9),
                ((10,), math.pi * 100),
                ((100,), math.pi * 10000),
                ((0.5,), math.pi * 0.25),
                ((1.3,), math.pi * 1.69),
)
self.perimeter_testcases = (
        ((0,), 0),
                ((1,), math.pi * 2),
                ((2,), math.pi * 4),
                ((3,), math.pi * 6),
                ((10,), math.pi * 20),
                ((100,), math.pi * 200),
                ((0.5,), math.pi),
                ((1.3,), math.pi * 2.6),
)
self.exception_testcases = (
        (('a',), self.module.area, TypeError),
                (('a',), self.module.perimeter, TypeError),
)
