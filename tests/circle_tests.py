import unittest
import circle

circle_testcase_area_perimeter = (
    # Values : radius, area, perimeter
    # Count tests : 17
    ("123",              None,                 None),
    (0.0,                0.0,                   0.0),

    (5.0,                78.53981633974483,     31.41592653589793),
    (12.3,               {123, 31},             None),
    (1,                  None,                  None),
    ((123, 312),         None,                  None),
    ([1, 2],             None,                  None),

    (108.62477365287467, 37068.724420093466,    682.5095818114503),
    (45.96375535230321,  6637.138517483991,     288.7987922923886),
    (117.55345075913621, 43413.08386947725,     738.6101146180637),
    (84.73442826008372,  22556.394394918727,    532.4021146560207),
    (96.80515438512832,  29440.612190466552,    608.2447236918897),

    (85.11074476318464,  22757.19099079883,     534.7665809791537),
    (72.20434827948586,  16378.592487243892,    453.6733002241432),
    (122.62775349104199, 47241.90664180985,     770.4928989873553),
    (117.54393043882953, 43406.052349347294,    738.5502966813931),
    (4.246416780640989, 56.649373009098916,     26.681023524284303),
)
class CircleTests(unittest.TestCase):
    def test_circle_area(self):
        for test in circle_testcase_area_perimeter:
            with self.subTest(test=test):
                if test[1] is not None:
                    self.assertEqual(circle.area(test[0]), test[1])
                else:
                    with self.assertRaises(TypeError):
                        circle.area(test[0])

    def test_circle_perimeter(self):
        for test in circle_testcase_area_perimeter:
            with self.subTest(test=test):
                if test[1] is not None:
                    self.assertEqual(circle.perimeter(test[0]), test[2])
                else:
                    with self.assertRaises(TypeError):
                        circle.perimeter(test[0])

if __name__ == '__main__':
    unittest.main()