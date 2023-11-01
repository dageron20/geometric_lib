import unittest
import math

import rectangle
import square
import triangle
import circle

class BaseAreaTestCase(object):
    '''
    ### Base test for area function
    1. There must be `self.module` attribute in your class.
    2. There must be `area(*args)` function in your `self.module` class/module.
    3. There should be `self.area_testcases` dict with test cases.
        Testcase format: `((arg1, arg2, arg3), answer)`
    4. Your TestCase class must be inherited from `unittest.TestCase` class.

    ```
    import unittest
    from test import BaseAreaTestCase
    
    class SquareTest(BaseAreaTestCase, unittest.TestCase):
        def setUp(self):
            self.module = myPackage.SquareClass
            self.area_testcases = (
                ((2, ), 4), # testcase 1
                ((70, ), 4900), # testcase 2
            )
    
    if __name__ == '__main__:
        unittest.main()
    ```
    '''
    def test_area(self):
        for inp, outp in self.area_testcases:
            result = self.module.area(*inp)
            self.assertEqual(
                result,
                outp,
                f'{self.module.__name__}:area\t{inp=} expected={outp} returned={result}'
            )

class BasePerimeterTestCase(object):
    '''
    ### Base test for perimeter function
    1. There must be `self.module` attribute in your class.
    2. There must be `perimeter(*args)` function in your `self.module` class/module.
    3. There should be `self.perimeter_testcases` dict with test cases.
        Testcase format: `((arg1, arg2, arg3), answer)`
    4. Your TestCase class must be inherited from `unittest.TestCase` class.

    ```
    import unittest
    from test import BasePerimeterTestCase
    
    class SquareTest(BasePerimeterTestCase, unittest.TestCase):
        def setUp(self):
            self.module = myPackage.SquareClass
            self.perimeter_testcases = (
                ((2, ), 8), # testcase 1
                ((100, ), 400), # testcase 2
            )
    
    if __name__ == '__main__:
        unittest.main()
    ```
    '''
    def test_perimeter(self):
        for inp, outp in self.perimeter_testcases:
            result = self.module.perimeter(*inp)
            self.assertEqual(
                result,
                outp,
                f'{self.module.__name__}:perimeter\t{inp=} expected={outp} returned={result}'
            )

class RectangleTest(BaseAreaTestCase, BasePerimeterTestCase, unittest.TestCase):
    '''
    ### UnitTests for `rectangle.py` module
    '''
    def setUp(self):
        self.module = rectangle
        self.area_testcases = (
            ((10, 0), 0),
            ((0, 0), 0),
            ((0, 10), 0),
            ((10, 10), 100),
            ((5, 5), 25),
            ((100, 100), 10000),
            ((5, 3), 15),
            ((3, 5), 15),
            ((100, 1), 100),
            ((1, 100), 100),
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
        )

class SquareTest(BaseAreaTestCase, BasePerimeterTestCase, unittest.TestCase):
    '''
    ### UnitTests for `square.py` module
    '''
    def setUp(self):
        self.module = square
        self.area_testcases = (
            ((10, ), 100),
            ((0, ), 0),
            ((1, ), 1),
            ((2, ), 4),
            ((70, ), 4900),
        )
        self.perimeter_testcases = (
            ((0, ), 0),
            ((1, ), 4),
            ((2, ), 8),
            ((100, ), 400),
            ((15, ), 60),
            ((3, ), 12),
        )

class TriangleTest(BaseAreaTestCase, BasePerimeterTestCase, unittest.TestCase):
    '''
    ### UnitTests for `triangle.py` module
    '''
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
        )

class CircleTest(BaseAreaTestCase, BasePerimeterTestCase, unittest.TestCase):
    '''
    ### UnitTests for `circle.py` module
    '''
    def setUp(self):
        self.module = circle
        self.area_testcases = (
            ((0, ), 0),
            ((1, ), math.pi),
            ((2, ), math.pi * 4),
            ((3, ), math.pi * 9),
            ((10, ), math.pi * 100),
            ((100, ), math.pi * 10000),
            ((0.5, ), math.pi * 0.25),
            ((1.3, ), math.pi * 1.69),
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
