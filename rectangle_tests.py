from rectangle import area, perimeter
import unittest


class RectangleTestCase(unittest.TestCase):
    def testAreaCalculation(self):
        self.assertEqual(area(5, 10), 50)

    def testPerimeterCalculation(self):
        self.assertEqual(perimeter(2, 8), 20)

    def testAreaNegative(self):
        self.assertEqual(area(-5, 10), "Length cannot be negative")

    def testPerimeterNegative(self):
        self.assertEqual(perimeter(2, -8), "Length cannot be negative")


if __name__ == "__main__":
    unittest.main()
