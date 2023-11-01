import unittest
import triangle


class TriangleTest(unittest.TestCase):
    def test_area_mul(self):
        for i in range(0, 100):
            for h in range(0, 100):
                res = triangle.area(i, h)
                if i == 0 or h == 0:
                    self.assertEqual(res, 0)
                else:
                    self.assertEqual(res, i * h / 2)

    def test_perimeter_mul(self):
        for a in range(0, 100):
            for b in range(0, 100):
                for c in range(0, 100):
                    res = triangle.perimeter(a, b, c)
                    if (a == 0 or b == 0 or c == 0) or ((a + b) <= c or (b + c) <= a or (a + c) <= b):
                        self.assertEqual(res, 0)
                    else:
                        self.assertEqual(res, a + b + c)


if __name__ == '__main__':
    unittest.main()