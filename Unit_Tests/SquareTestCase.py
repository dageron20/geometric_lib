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
        self.assertEqual(area(-10), "Negative side input in area()")

    def testPerimeterNegative(self):
        self.assertEqual(perimeter(-10), "Negative side input in perimeter()")

    def testAreaStr(self):
        self.assertEqual(area('xyz'), "Incorrect area() input (string)")

    def testPerimeterStr(self):
        self.assertEqual(perimeter('xyz'), "Incorrect perimeter() input (string)")

    def testAreaFloat(self):
        self.assertEqual(area(5.5), 30.25)

    def testPerimeterFloat(self):
        self.assertEqual(perimeter(5.5), 22)


if __name__ == "__main__":
    unittest.main()