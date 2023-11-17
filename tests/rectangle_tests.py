import unittest
import rectangle

rectangle_testcase_area_perimeter = (
    # Values : side, ground, area, perimeter
    # Count tests : 17
    (1.0,  "123",  None,   None),
    (0,      0,      0,      0),

    (67,     93,     6231,   320),
    (54,     16,     864,    140),
    (114,    11,     1254,   250),
    (111,    41,     4551,   304),
    (14,     63,     882,    154),

    (19,     121,    2299,   280),
    (96,     33,     3168,   258),
    (104,    112,    11648,  432),
    (69,     88,     6072,   314),
    (101,    83,     8383,   368),

    (96,     52,     4992,   296),
    (45,     38,     1710,   166),
    (77,     19,     1463,   192),
    (52,     46,     2392,   196),
    (31,     6,      186,    74),
)

class RectangleTests(unittest.TestCase):
    def test_rectangle_area(self):
        for test in rectangle_testcase_area_perimeter:
            with self.subTest(test=test):
                if test[2] is not None:
                    self.assertEqual(rectangle.area(test[0], test[1]), test[2])
                else:
                    with self.assertRaises(TypeError):
                        rectangle.area(test[0], test[1])

    def test_rectangle_perimeter(self):
        for test in rectangle_testcase_area_perimeter:
            with self.subTest(test=test):
                if test[3] is not None:
                    self.assertEqual(rectangle.perimeter(test[0], test[1]), test[3])
                else:
                    with self.assertRaises(TypeError):
                        rectangle.perimeter(test[0], test[1])

if __name__ == '__main__':
    unittest.main()

