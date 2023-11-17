from circle import area, perimeter
import unittest


class CircleTestCase(unittest.TestCase):
    def testAreaCalculation(self):
        self.assertEqual(area(5), 78)

    def testPerimeterCalculation(self):
        self.assertEqual(perimeter(5), 31)

    def testAreaNegative(self):
        self.assertEqual(area(-10), "Length cannot be negative")

    def testPerimeterNegative(self):
        self.assertEqual(perimeter(-10), "Length cannot be negative")


if __name__ == "__main__":
    unittest.main()
