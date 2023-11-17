from triangle import area, perimeter
import unittest


class TriangleTestCase(unittest.TestCase):
    def testAreaCalculation(self):
        self.assertEqual(area(10, 5), 25)

    def testPerimeterCalculation(self):
        self.assertEqual(perimeter(9, 7, 4), 20)

    def testAreaNegative(self):
        self.assertEqual(area(-10, 5), "Incorrect input")

    def testPerimeterNegative(self):
        self.assertEqual(perimeter(9, -7, 4), "Incorrect input")

    def testPerimeterIncorrectTriangle(self):
        self.assertEqual(perimeter(29, 4, 5), "Invalid size values")

    def testAreaFloat(self):
        self.assertEqual(area(0.5, 0.2), "Incorrect input")

    def testPerimeterFloat(self):
        self.assertEqual(perimeter(0.5, 0.3, 0.2), "Incorrect input")

    def testAreaStr(self):
        self.assertEqual(area('xyz', 'x'), "Incorrect input")

    def testPerimeterStr(self):
        self.assertEqual(perimeter('xyz', 'x', 'f'), "Incorrect input")


if __name__ == "__main__":
    unittest.main()
