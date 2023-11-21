import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from triangle import area, perimeter
import unittest

class TriangleTestCase(unittest.TestCase):
    def testAreaCalculation(self):
        self.assertEqual(area(10, 5), 25)

    def testPerimeterCalculation(self):
        self.assertEqual(perimeter(9, 7, 4), 20)

    def testAreaNegative(self):
        self.assertEqual(area(-1, 5), "Negative sides input in area()")

    def testPerimeterNegative(self):
        self.assertEqual(perimeter(8, -7, 3), "Negative sides input in perimeter()")

    def testPerimeterIncorrectTriangle(self):
        self.assertEqual(perimeter(22, 4, 3), "Invalid triangle sides values in perimeter()")

    def testAreaStr(self):
        self.assertEqual(area('xyz', 'z'), "Incorrect area() input (string)")

    def testPerimeterStr(self):
        self.assertEqual(perimeter('xyz', 'x', 'z'), "Incorrect perimeter() input (string)")


if __name__ == "__main__":
    unittest.main()
