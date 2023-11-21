import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from rectangle import area, perimeter
import unittest


class RectangleTestCase(unittest.TestCase):
    def testAreaCalculation(self):
        self.assertEqual(area(5, 10), 50)

    def testPerimeterCalculation(self):
        self.assertEqual(perimeter(2, 8), 20)

    def testAreaNegative(self):
        self.assertEqual(area(-5, 10), "Negative sides input in area()")

    def testPerimeterNegative(self):
        self.assertEqual(perimeter(2, -8), "Negative sides input in perimeter()")
        
    def testAreaStr(self):
        self.assertEqual(area('xyz', 'y'), "Incorrect area() input (string)")

    def testPerimeterStr(self):
        self.assertEqual(perimeter('xyz', 'q'), "Incorrect perimeter() input (string)")

    def testAreaFloat(self):
        self.assertEqual(area(5.5, 5.5), 30.25)

    def testPerimeterFloat(self):
        self.assertEqual(perimeter(5.5, 5.5), 22)

if __name__ == "__main__":
    unittest.main()