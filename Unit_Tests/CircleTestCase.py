import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from circle import area, perimeter
import unittest


class CircleTestCase(unittest.TestCase):
    def testAreaCalculation(self):
        self.assertEqual(area(5), 78.53981633974483)

    def testPerimeterCalculation(self):
        self.assertEqual(perimeter(5), 31.41592653589793)

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
        self.assertEqual(area(5.5), 95.03317777109123)

    def testPerimeterFloat(self):
        self.assertEqual(perimeter(5.5), 34.55751918948772)


if __name__ == "__main__":
    unittest.main()
