import unittest
from triangle import area
from triangle import perimeter

class TriangleTestCase(unittest.TestCase):
    #area test
    def test_area_regular_first(self):
        result = area(20, 45)
        self.assertEquals(result, 450)

    def test_area_regular_second(self):
        result = area(19, 7)
        self.assertEquals(result,66.5)

    def test_area_float_first(self):
        result = area(5.5, 10.5)
        self.assertEquals(result, 28.875)

    def test_area_float_second(self):
        result = area(325.5, 8)
        self.assertEquals(result, 1302)

    def test_area_zero(self):
        result = area(0, 10)
        self.assertEquals(result, 0)


    #perimeter test
    def test_perimeter_regular_first(self):
        result = perimeter(6,6,6)
        self.assertEquals(result, 18)

    def test_perimeter_regular_second(self):
        result = perimeter(50,100,1500)
        self.assertEquals(result, 1650)

    def test_perimeter_float_first(self):
        result = perimeter(100.5, 400.2, 200.1)
        self.assertEquals(result, 700.8)

    def test_perimeter_float_second(self):
        result = perimeter(200.4, 300.1, 2.2)
        self.assertEquals(result, 502.7)


