import unittest
import square


class SquareTest(unittest.TestCase):
    def test_area_mul(self):
        for i in range(0, 100):
            res = square.area(i)
            if i == 0:
                self.assertEqual(res, 0)
            else:
                self.assertEqual(res, i * i)

    def test_perimeter_mul(self):
        for i in range(0, 100):
            res = square.perimeter(i)
            if i == 0:
                self.assertEqual(res, 0)
            else:
                self.assertEqual(res, 4 * i)


if __name__ == '__main__':
    unittest.main()