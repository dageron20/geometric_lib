import unittest
from square import area
from square import perimeter

class SquareTestCase(unittest.TestCase):
    #area test
    def test_area_regular_first(self):
        result = area(10)
        self.assertEquals(result, 100)

    def test_area_regular_second(self):
        result = area(50)
        self.assertEquals(result, 2500)

    def test_area_float_first(self):
        result = area(5.3)
        self.assertEquals(result, 28.09)

    def test_area_float_second(self):
        result = area(200000.9)
        self.assertEquals(result, 40000360000.81)

    def test_area_zero(self):
        result = area(0)
        self.assertEquals(result, 0)

    #perimeter test
    def test_perimeter_regular_first(self):
        result = perimeter(6)
        self.assertEquals(result, 24)

    def test_perimeter_regular_second(self):
        result = perimeter(50)
        self.assertEquals(result, 200)

    def test_perimeter_float_first(self):
        result = perimeter(25.5)
        self.assertEquals(result, 102)

    def test_perimeter_float_second(self):
        result = perimeter(101.5)
        self.assertEquals(result, 406)

    def test_perimeter_zero(self):
        result = perimeter(0)
        self.assertEquals(result,0)

