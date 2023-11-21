import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from circle import area, perimeter
import unittest


class CircleTestCase(unittest.TestCase):
    def testAreaCalculation(self):
        self.assertEqual(area(5), 78)

    def testPerimeterCalculation(self):
        self.assertEqual(perimeter(5), 31)

    def testAreaNegative(self):
        self.assertEqual(area(-10), "Negative radius input in area()")

    def testPerimeterNegative(self):
        self.assertEqual(perimeter(-10), "Negative radius input in perimetr()")

    def testAreaStr(self):
        self.assertEqual(area('xyz'), "Incorrect area() input (string)")

    def testPerimeterStr(self):
        self.assertEqual(perimeter('xyz'), "Incorrect perimetr() input (string)")


if __name__ == "__main__":
    unittest.main()
