import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):
    #area test
    def test_area_regular_first(self):
        result = area(5, 4)
        self.assertEquals(result, 20)

    def test_area_regular_second(self):
        result = area(10000, 1)
        self.assertEquals(result,10000)

    def test_area_float_first(self):
        result = area(5.3, 10.8)
        self.assertEquals(result, 57.24)

    def test_area_float_second(self):
        result = area(28, 10.9)
        self.assertEquals(result, 305.2)

    def test_area_zero(self):
        result = area(5000, 0)
        self.assertEquals(result, 0)

    #perimeter test
    def test_perimeter_regular_first(self):
        result = perimeter(10, 15)
        self.assertEquals(result, 50)

    def test_perimeter_regular_second(self):
        result = perimeter(50, 20)
        self.assertEquals(result, 140)

    def test_perimeter_float_first(self):
        result = perimeter(20.5, 55.9)
        self.assertEquals(result, 152.8)

    def test_perimeter_float_second(self):
        result = perimeter(55.2, 100.2)
        self.assertEquals(result, 310.8)


