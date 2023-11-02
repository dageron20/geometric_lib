import unittest
from rectangle import area, perimeter


class TestRectangle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(5, 2), 5 * 2)
        self.assertEqual(area(100, 123647), (100 * 123647))
        self.assertEqual(area(10 ** 5, 10 ** 6), (10 ** 5) * (10 ** 6))
        self.assertEqual(area(10 ** 6, 999909374834759), (10 ** 6) * 999909374834759)
        self.assertEqual(area(23553456798747354674857, 10 ** 6), (10 ** 6) * 23553456798747354674857)
        self.assertEqual(area(1.2, 1.2345245646), 1.2 * 1.2345245646)
        self.assertEqual(area(23243554.242547468344763823, 0.183712738647832646252784263287),
                         23243554.242547468344763823 * 0.183712738647832646252784263287)
        self.assertEqual(area(250.9999999, 0.0000000000000939838576), 250.9999999 * 0.0000000000000939838576)
        self.assertEqual(area(0.128371947, 1000000.666666), 0.128371947 * 1000000.666666)
        self.assertEqual(area(0.98765, 219382917437.00000001232137), 0.98765 * 219382917437.00000001232137)
        self.assertEqual(area(-10, 302938.0892137), 'Не корректные входные данные')
        self.assertEqual(area('a', 7813673437), 'Не корректные входные данные')
        self.assertEqual(area(0., 12453), 'Не корректные входные данные')
        self.assertEqual(area(0, 2), 'Не корректные входные данные')

    def test_perimetr(self):
        self.assertEqual(perimeter(5, 2), 5 * 2 + 2 * 2)
        self.assertEqual(perimeter(100, 123647), 2 * (100 + 123647))
        self.assertEqual(perimeter(10 ** 5, 10 ** 6), 2 * ((10 ** 5) + (10 ** 6)))
        self.assertEqual(perimeter(10 ** 6, 999909374834759), 2 * ((10 ** 6) + 999909374834759))
        self.assertEqual(perimeter(23553456798747354674857, 10 ** 6), 2 * ((10 ** 6) + 23553456798747354674857))
        self.assertEqual(perimeter(1.2, 1.2345245646), 2 * (1.2 + 1.2345245646))
        self.assertEqual(perimeter(23243554.242547468344763823, 0.183712738647832646252784263287),
                         2 * (23243554.242547468344763823 + 0.183712738647832646252784263287))
        self.assertEqual(perimeter(250.9999999, 0.0000000000000939838576), 2 * (250.9999999 + 0.0000000000000939838576))
        self.assertEqual(perimeter(0.128371947, 1000000.666666), 2 * (0.128371947 + 1000000.666666))
        self.assertEqual(perimeter(0.98765, 219382917437.00000001232137), 2 * (0.98765 + 219382917437.00000001232137))
        self.assertEqual(perimeter(-10, 302938.0892137), 'Не корректные входные данные')
        self.assertEqual(perimeter('a', 7813673437), 'Не корректные входные данные')
        self.assertEqual(perimeter(0., 12453), 'Не корректные входные данные')
        self.assertEqual(perimeter(0, 2), 'Не корректные входные данные')
