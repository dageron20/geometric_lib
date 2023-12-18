import unittest
def area(a, b):
    '''Возвращает площадь прямоугольника

        Параметры:
            a (int) or (float):Сторона прямоугольника
            b (int) or (float):Сторона прямоугольника

        Возвращаемое значение:
            (int) or (float):Площадь данного прямоугольника
    ''' 
    return a * b 

def perimeter(a, b):  
    '''Возвращает периметр прямоугольника
    
        Параметры:
            a (int) or (float):Сторона прямоугольника
            b (int) or (float):Сторона прямоугольника

        Возвращаемое значение:
            (int) or (float):Периметр данного прямоугольника
    '''   
    return 2 * (a + b)
class RectangleTestCase(unittest.TestCase):
    #area test
    def test_area_int(self):
        res = area(125, 56)
        self.assertEqual(res, 7000)
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_rectangle_area_double(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
    def test_rectangle_area_big_data(self):
        res = area(347889382374, 8380983389992)
        self.assertEqual(res, 2915655135231069652801008)

    def test_rectangle_area_fraction(self):
        res = area(45.678, 21.5678)
        self.assertEqual(res, 985.1739683999998)

    # perimetr test
    def test_perimetr_int(self):
        res = perimeter(28, 18)
        self.assertEqual(res, 92)
    def test_zero_perimetr(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_rectangle_perimetr_double(self):
        res = perimeter(45, 45)
        self.assertEqual(res, 180)
    def test_rectangle_perimetr_big_data(self):
        res = perimeter(347889382374, 8380983389992)
        self.assertEqual(res, 17457745544732)

    def test_rectangle_perimetr_fraction(self):
        res = perimeter(789.123, 11.146)
        self.assertEqual(res, 1600.538)
