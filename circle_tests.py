from circle import area, perimeter
import unittest


class CircleTestCase(unittest.TestCase):
    def testAreaCalculation(self):
        self.assertEqual(area(5), 78)

    def testPerimeterCalculation(self):
        self.assertEqual(perimeter(5), 31)

    def testAreaNegative(self):
        self.assertEqual(area(-10), "Incorrect input")

    def testPerimeterNegative(self):
        self.assertEqual(perimeter(-10), "Incorrect input")

    def testAreaFloat(self):
        self.assertEqual(area(0.5), "Incorrect input")

    def testPerimeterFloat(self):
        self.assertEqual(perimeter(0.5), "Incorrect input")

    def testAreaStr(self):
        self.assertEqual(area('xyz'), "Incorrect input")

    def testPerimeterStr(self):
        self.assertEqual(perimeter('xyz'), "Incorrect input")


if __name__ == "__main__":
    unittest.main()
