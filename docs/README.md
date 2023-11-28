# Общее описание решения
Библиотека добавляет математические формулы для вычисления площади и периметра различных геометрических фигур
# Math formulas
## Area
- Формула для вычисления площади круга  
    Circle: S = πR²

    def area(r):  
        return math.pi * r * r

    Принимает число r, возвращает произведение числа pi и квадрата этого числа.

    Пример:   
    r = 10  
    area(r) == 314,15926535897932384626433832795
- Формула для вычисления площади прямоугольника  
    Rectangle: S = ab

    def area(a, b):   
        return a * b

    Принимает числа a и b, возвращает их произведение.

    Пример:   
    a = 5  
    b = 4  
    area(a,b) == 20
- Формула для вычисления площади квадрата  
    Square: S = a²  

    def area(a):  
        return a * a

    Принимает число a, возвращает квадрат этого числа.

    Пример:   
    a = 5  
    area(a) == 25
- Формула для вычисления площади треугольника  
    Triangle: S = (a*h) / 2

    def area(a, h):  
        return a * h / 2 
    
    Принимает числа a и h, вовращает произведние этих чисел, деленное на два.

    Пример:   
    a = 5  
    h = 4  
    area(a, h) == 10
## Perimeter
- Формула для вычисления периметра круга  
    Circle: P = 2πR

    def perimeter(r):  
        return 2 * math.pi * r

    Принимает число r, возвращает произведение этого числа, числа pi и 2.

    Пример:   
    r = 10  
    perimeter(r) == 62,83185307179586476925286766559
- Формула для вычисления периметра прямоугольника  
    Rectangle: P = 2a + 2b

    def perimeter(a, b):   
        return (a + b)*2  

    Принимает числа a и b, возвращает их сумму, умноженую на 2.

    Пример:   
    a = 5  
    b = 4  
    perimeter(a, b) == 18
- Формула для вычисления периметра квадрата  
    Square: P = 4a

    def perimeter(a):  
        return 4 * a

    Принимает число a, возвращает это число, умноженое на 4.

    Пример:   
    a = 5  
    perimeter(a) == 20
- Формула для вычисления периметра треугольника  
    Triangle: P = a + b + c

    def perimeter(a, b, c):   
        return a + b + c

    Принимает числа a, b и c, вовращает сумму этих чисел.

    Пример:  
    a = 5  
    b = 3  
    c = 2  
    perimeter(a, b, c) == 10
# История коммитов
- commit 5577037b807c0f02b08293086e3c2d46ed00080a  
    Исправлена ошибка отображения.
- commit 9727c36cbb8319ea53f2b5877c54258f4ba3f292  
    Добавлена документация
- commit 3f9a880449e5a8bbdf343c970c137d6bf25a4cc0  
    Добавлен Файл triangle.py. Иправлена ошибка в файле rectangle.py
- commit cc8fdc9b3756155b0414f789b4bf1c24d95748ef    
    Добавлен файл rectangle.py
- commit d078c8d9ee6155f3cb0e577d28d337b791de28e2  
    L-03: Docs added
- commit 8ba9aeb3cea847b63a91ac378a2a6db758682460  
    L-03: Circle and square added
# Тесты
| Tests                  | Input     | Expected output       | Result    |
|------------------------|-----------|-----------------------|-----------|
|**RECTANGLE_TESTS**     |           |                       | Passed    |
|test_normal_area        | 0.7, 10   | 7                     | Passed    |
|test_normal_perimeter   | 10, 10    | 40                    | Passed    |
|test_negative_area      | 10, -1    | Negative arguments    | Passed    |
|test_negative_perimiter | 10, -1    | Negative arguments    | Passed    |
|test_area_char          | 'c', 3    | Non-integer arguments | Passed    |
|test_perimeter_char     | 'c', 5    | Non-integer arguments | Passed    |
|**CIRCLE_TESTS**        |           |                       | Passed    |
|test_normal_area        | 10        | 314.159265358979323   | Passed    |
|test_normal_perimeter   | 10        | 62.8318530717958647   | Passed    |
|test_negative_area      | -1        | Negative arguments    | Passed    |
|test_negative_perimiter | -1        | Negative arguments    | Passed    |
|test_area_char          | 'c'       | Non-integer arguments | Passed    |
|test_perimeter_char     | 'c'       | Non-integer arguments | Passed    |
|**TRIANGLE_TESTS**      |           |                       | Passed    |
|test_normal_area        | 5, 4      | 10                    | Passed    |
|test_normal_perimeter   | 10, 10, 5 | 25                    | Passed    |
|test_negative_area      | -8, 5     | Negative arguments    | Passed    |
|test_negative_perimiter | 10, -1, 7 | Negative arguments    | Passed    |
|test_area_char          | 'c', 2    | Non-integer arguments | Passed    |
|test_perimeter_char     | 'c', 2, 3 | Non-integer arguments | Passed    |
|**SQUARE_TESTS**        |           |                       | Passed    |
|test_normal_area        | 10        | 100                   | Passed    |
|test_normal_perimeter   | 10        | 40                    | Passed    |
|test_negative_area      | -10       | Negative arguments    | Passed    |
|test_negative_perimiter | -3        | Negative arguments    | Passed    |
|test_area_char          | 'c'       | Non-integer arguments | Passed    |
|test_perimeter_char     | 'c'       | Non-integer arguments | Passed    |

