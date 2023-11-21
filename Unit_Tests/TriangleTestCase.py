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
        with self.assertRaises(Exception):
            area(-1, 5)

    def testPerimeterNegative(self):
        with self.assertRaises(Exception):
            perimeter(8, -7, 3)

    def testPerimeterIncorrectTriangle(self):
        with self.assertRaises(Exception):
            perimeter(22, 4, 3)

    def testAreaStr(self):
        with self.assertRaises(TypeError):
            area('xyz', 'z')

    def testPerimeterStr(self):
        with self.assertRaises(TypeError):
            perimeter('xyz', 'x', 'z')

    def testAreaFloat(self):
        self.assertEqual(area(10.5, 2.5), 13.125)

    def testPerimeterFloat(self):
        self.assertEqual(perimeter(5.5, 5.5, 5.5), 16.5)

if __name__ == "__main__":
    unittest.main()
