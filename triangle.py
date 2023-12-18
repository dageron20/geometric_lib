import unittest
def area(a, h):
    '''Возвращает площадь треугольника

        Параметры:
            a (int) or (float):Сторона треугольника 
            h (int) or (float):Высота опущенная к стороне треугольника
        Возвращаемое значение:
            (int) or (float):Площадь данного треугольника
    ''' 
    return a * h / 2 

def perimeter(a, b, c):
    '''Возвращает периметр треугольника
    
        Параметры:
            a (int) or (float):Сторона треугольника 
            b (int) or (float):Сторона треугольника
            c (int) or (float):Сторона треугольника
        Возвращаемое значение:
            (int) or (float):Периметр данного треугольника
    ''' 
    return a + b + c
class Triangle_TestCase(unittest.TestCase):
    #area test
    def test_area_int(self):
        res = area(3216, 349)
        self.assertEqual(res, 561192.0)
    def test_zero_side_area(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_zero_height_area(self):
        res = area(5, 0)
        self.assertEqual(res, 0)
    def test_triangle_area_big_data(self):
        res = area(9423847329131, 84823929121)
        self.assertEqual(res, 3.9968387894666656e+23)

    def test_triangle_area_fraction(self):
        res = area(2439.999, 14.3136)
        self.assertEqual(res, 17462.5848432)

    # perimetr test
    def test_perimetr_int(self):
        res = perimeter(63, 56, 89)
        self.assertEqual(res, 208)
    def test_zero_perimetr(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_zero_one_side_perimetr(self):
        res = perimeter(0, 4, 8)
        self.assertEqual(res, 12)
    def test_triangle_perimetr_big_data(self):
        res = perimeter(46544561578, 32690642383, 5785126333457)
        self.assertEqual(res, 5864361537418)

    def test_square_perimetr_fraction(self):
        res = perimeter(67.8963, 320.124005, 1221.511889)
        self.assertEqual(res, 1609.5321940000001)