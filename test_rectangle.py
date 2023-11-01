import unittest
import rectangle


class RectangleTest(unittest.TestCase):
    def test_area_mul(self):
        for i in range(0, 100):
            for j in range(0, 100):
                res = rectangle.area(i, j)
                self.assertEqual(res, i * j)

    def test_perimeter_mul(self):
        for i in range(0, 100):
            for j in range(0, 100):
                res = rectangle.perimeter(i, j)
                if i == 0 or j == 0:
                    self.assertEqual(res, 0)
                else:
                    self.assertEqual(res, 2 * (i + j))


if __name__ == '__main__':
    unittest.main()
