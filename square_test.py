import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(2), 2 * 2)
        self.assertEqual(area(100), 100 * 100)
        self.assertEqual(area(10 ** 6), (10 ** 6) * (10 ** 6))
        self.assertEqual(area(999909374834759), 999909374834759 * 999909374834759)
        self.assertEqual(area(23553456798747354674857), 23553456798747354674857 * 23553456798747354674857)
        self.assertEqual(area(1.2345245646), 1.2345245646 * 1.2345245646)
        self.assertEqual(area(0.183712738647832646252784263287),
                         0.183712738647832646252784263287 * 0.183712738647832646252784263287)
        self.assertEqual(area(0.0000000000000939838576), 0.0000000000000939838576 * 0.0000000000000939838576)
        self.assertEqual(area(0.128371947), 0.128371947 * 0.128371947)
        self.assertEqual(area(219382917437.00000001232137),
                         219382917437.00000001232137 * 219382917437.00000001232137)
        self.assertEqual(area(-10), 'Не корректные входные данные')
        self.assertEqual(area('a'), 'Не корректные входные данные')
        self.assertEqual(area(0.), 'Не корректные входные данные')
        self.assertEqual(area(0), 'Не корректные входные данные')

    def test_perimetr(self):
        self.assertEqual(perimeter(2), 2 * 4)
        self.assertEqual(perimeter(100), 100 * 4)
        self.assertEqual(perimeter(10 ** 6), 4 * 10 ** 6)
        self.assertEqual(perimeter(999909374834759), 4 * 999909374834759)
        self.assertEqual(perimeter(23553456798747354674857), 4 * 23553456798747354674857)
        self.assertEqual(perimeter(1.2345245646), 4 * 1.2345245646)
        self.assertEqual(perimeter(0.183712738647832646252784263287), 4 * 0.183712738647832646252784263287)
        self.assertEqual(perimeter(0.0000000000000939838576), 4 * 0.0000000000000939838576)
        self.assertEqual(perimeter(0.128371947), 4 * 0.128371947)
        self.assertEqual(perimeter(219382917437.00000001232137), 4 * 219382917437.00000001232137)
        self.assertEqual(perimeter(-10), 'Не корректные входные данные')
        self.assertEqual(perimeter('a'), 'Не корректные входные данные')
        self.assertEqual(perimeter(0.), 'Не корректные входные данные')
        self.assertEqual(perimeter(0), 'Не корректные входные данные')
