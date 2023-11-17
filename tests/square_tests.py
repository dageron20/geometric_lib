import unittest
import square


square_testcase_area_perimeter = (
    # Values : side, area, perimeter
    # Count tests : 17
    ((1, 2),  None,   None),
    (0,      0,      0),

    (99.123,         None,   None),
    ("43",           None,   None),
    ([1, 2],         None,   None),
    ((9.0, 5.0),     None,   None),
    (42,             1764,   168),

    (58,     3364,   232),
    (86,     7396,   344),
    (9,      81,     36),
    (40,     1600,   160),
    (86,     7396,   344),

    (40,     1600,   160),
    (119,    14161,  476),
    (22,     484,    88),
    (81,     6561,   324),
    (48,     2304,   192),
)

class SquareTests(unittest.TestCase):
    def test_square_area(self):
        for test in square_testcase_area_perimeter:
            with self.subTest(test=test):
                if test[1] is not None:
                    self.assertEqual(square.area(test[0]), test[1])
                else:
                    with self.assertRaises(TypeError):
                        square.area(test[0])

    def test_square_perimeter(self):
        for test in square_testcase_area_perimeter:
            with self.subTest(test=test):
                if test[1] is not None:
                    self.assertEqual(square.perimeter(test[0]), test[2])
                else:
                    with self.assertRaises(TypeError):
                        square.perimeter(test[0])

if __name__ == '__main__':
    unittest.main()