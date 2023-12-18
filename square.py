import unittest
def area(a):
    '''Возвращает площадь квадрата

        Параметры:
            a (int) or (float):Сторона квадрата 
        Возвращаемое значение:
            (int) or (float):Площадь данного квадрата
    ''' 
    return a * a


def perimeter(a):
    '''Возвращает периметр квадрата
    
        Параметры:
            a (int) or (float):Сторона квадрата 
        Возвращаемое значение:
            (int) or (float):Периметр данного квадрата
    ''' 
    return 4 * a
class Square_TestCase(unittest.TestCase):
    #area test
    def test_area_int(self):
        res = area(789)
        self.assertEqual(res, 622521)
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_area_one(self):
        res = area(1)
        self.assertEqual(res, 1)
    def test_square_area_big_data(self):
        res = area(77634100891)
        self.assertEqual(res, 6027053621153966993881)

    def test_square_area_fraction(self):
        res = area(4567.3421)
        self.assertEqual(res, 20860613.85843241)

    # perimetr test
    def test_perimetr_int(self):
        res = perimeter(91)
        self.assertEqual(res, 364)
    def test_zero_perimetr(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_square_perimetr_one(self):
        res = perimeter(1)
        self.assertEqual(res, 4)
    def test_square_perimetr_big_data(self):
        res = perimeter(457997155624564456)
        self.assertEqual(res, 1831988622498257824)

    def test_square_perimetr_fraction(self):
        res = perimeter(443.67865)
        self.assertEqual(res, 1774.7146)
