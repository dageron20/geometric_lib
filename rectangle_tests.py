from rectangle import area, perimeter
import unittest


class RectangleTestCase(unittest.TestCase):
    def testAreaCalculation(self):
        self.assertEqual(area(5, 10), 50)

    def testPerimeterCalculation(self):
        self.assertEqual(perimeter(2, 8), 20)

    def testAreaNegative(self):
        self.assertEqual(area(-5, 10), "Incorrect input")

    def testPerimeterNegative(self):
        self.assertEqual(perimeter(2, -8), "Incorrect input")

    def testAreaFloat(self):
        self.assertEqual(area(0.5, 0.2), "Incorrect input")

    def testPerimeterFloat(self):
        self.assertEqual(perimeter(0.5, 0.6), "Incorrect input")

    def testAreaStr(self):
        self.assertEqual(area('xyz', 'y'), "Incorrect input")

    def testPerimeterStr(self):
        self.assertEqual(perimeter('xyz', 'q'), "Incorrect input")

if __name__ == "__main__":
    unittest.main()
