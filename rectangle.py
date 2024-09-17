def area(a, b):
    """ Возвращает площадь прямоугольника.
               Параметры:
                    a, b (int, float) : соседние стороны прямоугольника
               Возвращаемое значение:
                   a*b (int, float) : значение площади прямоугольника размера axb"""
    if(type(a) not in [float,int] or type(b) not in[float,int] or a<=0 or b<=0):
        return 'Не корректные входные данные'
    else:
        return a * b

def perimeter(a, b):
    """ Возвращает периметр прямоугольника.
                   Параметры:
                        a, b (int, float) : соседние стороны прямоугольника
                   Возвращаемое значение:
                       2*a + 2*b (int, float) : значение периметра прямоугольника размера axb"""
    if (type(a) not in [float, int] or type(b) not in [float, int] or a <= 0 or b <= 0):
        return 'Не корректные входные данные'
    else:
        return 2*a + (2*b)