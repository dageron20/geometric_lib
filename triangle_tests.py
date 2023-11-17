from triangle import area, perimeter
import unittest


class TriangleTestCase(unittest.TestCase):
    def testAreaCalculation(self):
        self.assertEqual(area(10, 5), 25)

    def testPerimeterCalculation(self):
        self.assertEqual(perimeter(9, 7, 4), 20)

    def testAreaNegative(self):
        self.assertEqual(area(-10, 5), "Length cannot be negative")

    def testPerimeterNegative(self):
        self.assertEqual(perimeter(9, -7, 4), "Length cannot be negative")

    def testPerimeterIncorrectTriangle(self):
        self.assertEqual(perimeter(29, 4, 5), "Invalid size values")


if __name__ == "__main__":
    unittest.main()
