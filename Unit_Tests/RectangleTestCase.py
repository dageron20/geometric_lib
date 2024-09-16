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
        with self.assertRaises(Exception):
            area(-5, 10)

    def testPerimeterNegative(self):
        with self.assertRaises(Exception):
            perimeter(2, -8)
        
    def testAreaStr(self):
        with self.assertRaises(TypeError):
            area('xyz', 'y')

    def testPerimeterStr(self):
        with self.assertRaises(TypeError):
            perimeter('xyz', 'q')

    def testAreaFloat(self):
        self.assertEqual(area(5.5, 5.5), 30.25)

    def testPerimeterFloat(self):
        self.assertEqual(perimeter(5.5, 5.5), 22)

if __name__ == "__main__":
    unittest.main()