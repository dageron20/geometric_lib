import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from square import area, perimeter
import unittest

class SquareTestCase(unittest.TestCase):
    def testAreaCalculation(self):
        self.assertEqual(area(5), 25)

    def testPerimeterCalculation(self):
        self.assertEqual(perimeter(4), 16)

    def testAreaNegative(self):
        with self.assertRaises(Exception):
            area(-10)

    def testPerimeterNegative(self):
        with self.assertRaises(Exception):
            perimeter(-10)

    def testAreaStr(self):
        with self.assertRaises(TypeError):
            area('xyz')

    def testPerimeterStr(self):
        with self.assertRaises(TypeError):
            perimeter('xyz')

    def testAreaFloat(self):
        self.assertEqual(area(5.5), 30.25)

    def testPerimeterFloat(self):
        self.assertEqual(perimeter(5.5), 22)


if __name__ == "__main__":
    unittest.main()