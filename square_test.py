import unittest
import square


class SquareTest(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(area(3), 9)
    def test_area_2(self):
        self.assertEqual(area(0), "Doesn't exist")
    def test_area_3(self):
        self.assertEqual(area(-3), "Doesn't exist")
    def test_area_4(self):
        self.assertEqual(area(True), "Incorrect input")
    def test_area_5(self):
        self.assertEqual(area('mw'), "Incorrect input")

    def test_perimeter_1(self):
        self.assertEqual(perimeter(3), 12)
    def test_perimeter_2(self):
        self.assertEqual(perimeter(0), "Doesn't exist")
    def test_perimeter_3(self):
        self.assertEqual(perimeter(-3), "Doesn't exist")
    def test_perimeter_4(self):
        self.assertEqual(perimeter(True), "Incorrect input")
    def test_perimeter_5(self):
        self.assertEqual(perimeter("mw"), "Incorrect input")


if __name__ == '__main__':
    unittest.main()
