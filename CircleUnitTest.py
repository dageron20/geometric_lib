import unittest
from circle import area
from circle import perimeter

class CircleTestCase(unittest.TestCase):
    #area test
    def test_area_regular_first(self):
        result = area(5)
        self.assertEquals(result, 78.53981633974483)

    def test_area_regular_second(self):
        result = area(65)
        self.assertEquals(result,13273.228961416875)

    def test_area_float_first(self):
        result = area(5.3)
        self.assertEquals(result, 88.24733763933727)

    def test_area_float_second(self):
        result = area(30.6)
        self.assertEquals(result, 2941.661697115339)

    def test_area_zero(self):
        result = area(0)
        self.assertEquals(result, 0)

    #perimeter test
    def test_perimeter_regular_first(self):
        result = perimeter(6)
        self.assertEquals(result, 37.69911184307752)

    def test_perimeter_regular_second(self):
        result = perimeter(50)
        self.assertEquals(result, 314.1592653589793)

    def test_perimeter_float_first(self):
        result = perimeter(25.5)
        self.assertEquals(result, 160.22122533307945)

    def test_perimeter_float_second(self):
        result = perimeter(101.5)
        self.assertEquals(result, 637.743308678728)

    def test_perimeter_zero(self):
        result = perimeter(0)
        self.assertEquals(result,0)

