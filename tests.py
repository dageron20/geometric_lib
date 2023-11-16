import unittest
import math
import rectangle
import square
import circle
import triangle

class PerimetrAreaTestCase(object):

    def test_perimetr(self):
        for inp, outp in self.perimetr_testcases:
            result = self.module.perimetr(*inp)
            self.assertEqual(
                result,
                outp,
                f'{self.module.__name__}:perimetr\t{inp=} expected={outp} returned={result}'
            )

    def test_area(self):
        for inp, outp in self.area_testcases:
            result = self.module.area(*inp)
            self.assertEqual(
                result,
                outp,
                f'{self.module.__name__}:area\t{inp=} expected={outp} returned={result}'
            )


class RectangleTestCase(PerimetrAreaTestCase, unittest.TestCase):
    def setUp(self):
        self.module = rectangle
        
        self.area_testcases = (
            ((10, 0), 0), 
            (("a", 3), TypeError), 
            ((-3, 10), ValueError),
            ((10, 10), 100),
            ((5, 5), 25),
            ((100, 100), 10000),
            ((5, 3), 15)
        )

        self.perimetr_testcases = (
            (('a', 2), TypeError),
            ((5, 4), 18),
            ((10, 0), 20),
            ((-1, 10), ValueError),
            ((10, 10), 40)
        )

class TriangleTestCase(PerimetrAreaTestCase, unittest.TestCase):
    def setUp(self):
        self.module = triangle
        
        self.area_testcases = (
            ((-10, 8), ValueError),
            (('a', 7), TypeError),
            ((7, 8), 28)
        )

        self.perimetr_testcases = (
            (('a', 'b', 'c'), TypeError),
            ((-23, 1, 4), ValueError),
            ((9, 8, 4), 21),
            ((-2, 3, 0), ValueError),
            ((1000, 1000, 1000), 3000),
        )

class SquareTestCase(PerimetrAreaTestCase, unittest.TestCase):
    def setUp(self):

        self.module = square

        self.area_testcases = (
            (('a', ), TypeError),
            ((-5, ), ValueError),
            ((10, ), 100),
            ((-2, ), ValueError),
            ((1000, ), 1000000),
        )

        self.perimetr_testcases = (
            (('a', ), TypeError),
            ((-2, ), ValueError),
            ((2, ), 8),
            ((100, ), 400),
            ((15, ), 60),
            ((3, ), 12),
            ((1000, ), 4000),
        )
class CircleTestCase(PerimetrAreaTestCase, unittest.TestCase):
    def setUp(self):
        
        self.module = circle

        self.perimetr_testcases = (
            ((-2, ), ValueError),
            ((5, ),  10 * math.pi),
            (('a', ), TypeError),
            ((1000, ), 2000 * math.pi)
        )

        self.area_testcases = (
            ((3, ), math.pi * 9),
            (('a', ), TypeError),
            ((1000, ), math.pi * 1000000)
        )

        

if __name__ == "__main__":
    unittest.main()