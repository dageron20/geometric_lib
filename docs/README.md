# Введение
Geometric Lib - библиотека геометрических вычислений, разработанная для работы с различными геометрическими объектами и операциями над ними.
# Описание функций
## Функции для круга
Функция area принимает число r - радиус и возвращает площадь круга.
```python
def area(r):
    return math.pi * r * r
```
Функция perimeter принимает число r - радиус и возвращает периметр круга.
```py
def perimeter(r):
    
    return 2 * math.pi * r
```
Пример вызова:
```python
print(area(15))
print(perimeter(15))
```
Выходные данные:
```py
706.8583470577034
94.24777960769379
```
## Функции для квадрата
Функция area принимает число а - сторону квадрата и возвращает его площадь.
```python
def area(a):
    return a * a

```

Функция perimeter принимает число а - сторону квадрата и возвращает его периметр.
```py
def perimeter(a):
    return 4 * a
```
Пример вызова:
```python
print(area(7))
print(perimeter(7))
```
Выходные данные:
```py
49
28
```
## Функции для трапеции
Функция area  принимает длины двух оснований - a, b и высоту трапеции - h, возвращает ее площадь.
```python
def area(a, b, h):
    return (a + b) * h / 2
```

Функция perimeter принимает длины двух оснований - a, b и длины двух боковых сторон - c, d трапеции и возвращает ее периметр.
```py
def perimeter(a, b, c, d):
    return a + b + c + d
```
Пример вызова:
```python
print(area(10, 4, 4))
print(perimeter(10, 4, 5, 5))
```
Выходные данные:
```py
28
24
```
## Функции для треугольника
Функция area принимает длину основания треугольника - a и его высоту - h, возвращает его площадь.
```python
def area(a, h):
    return a * h / 2
```

Функция perimeter принимает длины трех сторон треугольника - a, b, c, возвращает его периметр.
```py
def perimeter(a, b, c):
    return a + b + c
```
Пример вызова:
```python
print(area(12, 8))
print(perimeter(7, 8, 6))
```
Выходные данные:
```py
48
21
```
# История изменений проекта
```
* 34c624130c4f2f4ba13cca2ce7ef633c1544ba30 (HEAD -> main, origin/main, origin/HEAD) New file triangle.py is added and trapeze area formula bug is fixed
* 15a70b796c9656fc0beb719bfe4aedab5433a17c New file trapeze.py is added
* d078c8d9ee6155f3cb0e577d28d337b791de28e2 L-03: Docs added
* 8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added
```
##  Тесты
| Название                               | Входные данные                     | Ожидаемый результат | Результат прохождения теста |
|----------------------------------------|------------------------------------|---------------------|-----------------------------|
| **Square Tests**                       |                                    |                     |                             |
| test_square_zero_area                  | 0                                  | 0                   | Passed                      |
| test_square_zero_perimeter             | 0                                  | 0                   | Passed                      |
| text_square_mul_digit_area             | 253                                | 64009               | Passed                      |
| test_square_mul_digit_perimeter        | 253                                | 1012                | Passed                      |
| test_square_single_digit_area          | 1                                  | 1                   | Passed                      |
| test_square_single_digit_perimeter     | 5                                  | 20                  | Passed                      |
| test_square_fraction_area              | 5.25                               | 27.5625             | Passed                      |
| test_square_fraction_perimeter         | 1.1                                | 4.4                 | Passed                      |
| test_square_negative_digit_area        | -5                                 | 0                   | Failed                      |
| test_square_negative_digit_perimeter   | -520                               | 0                   | Failed                      |
| test_square_string_area                | "5"                                | 25                  | Failed                      |
| test_square_string_perimeter           | "250"                              | 1000                | Failed                      |
| **Circle Tests**                       |                                    |                     |                             |
| test_circle_zero_area                  | 0                                  | 0                   | Passed                      |
| test_circle_zero_perimeter             | 0                                  | 0                   | Passed                      |
| text_circle_mul_digit_area             | 23                                 | 1661.9025137490005  | Passed                      |
| test_circle_mul_digit_perimeter        | 23                                 | 144.51326206513048  | Passed                      |
| test_circle_single_digit_area          | 2                                  | 12.566370614359172  | Passed                      |
| test_circle_single_digit_perimeter     | 2                                  | 12.566370614359172  | Passed                      |
| test_circle_fraction_area              | 5.5                                | 95.03317777109123   | Passed                      |
| test_circle_fraction_perimeter         | 5.5                                | 34.55751918948772   | Passed                      |
| test_circle_negative_digit_area        | -5                                 | 0                   | Failed                      |
| test_circle_negative_digit_perimeter   | -20                                | 0                   | Failed                      |
| test_circle_string_area                | "5"                                | 78.53981633974483   | Failed                      |
| test_circle_string_perimeter           | "5"                                | 31.41592653589793   | Failed                      |
| **Triangle Tests**                     |                                    |                     |                             |
| test_triangle_zero_area                | a = 0, h = 3                       | 0                   | Passed                      |
| test_triangle_zero_perimeter           | a = 5, b = 0, c = 6                | 0                   | Failed                      |
| text_triangle_mul_digit_area           | a = 23, h = 12                     | 138                 | Passed                      |
| test_triangle_mul_digit_perimeter      | a = 23, b = 71, c = 55             | 149                 | Passed                      |
| test_triangle_single_digit_area        | a = 2, h = 6                       | 6                   | Passed                      |
| test_triangle_single_digit_perimeter   | a = 2, b = 7, c = 5                | 14                  | Passed                      |
| test_triangle_fraction_area            | a = 5.25, h = 6                    | 15.75               | Passed                      |
| test_triangle_fraction_perimeter       | a = 2.4, b = 7.5, c = 5            | 14.9                | Passed                      |
| test_triangle_negative_digit_area      | a = -5, h = 3                      | 0                   | Failed                      |
| test_triangle_negative_digit_perimeter | a = -2, b = 7, c = 6               | 0                   | Failed                      |
| test_triangle_string_area              | a = "5", h = "6"                   | 15                  | Failed                      |
| test_triangle_string_perimeter         | a = "6", b = "3", c = "7"          | 16                  | Failed                      |
| **Trapeze Tests**                      |                                    |                     |                             |
| test_trapeze_zero_area                 | a = 0, b = 3, h = 7                | 0                   | Failed                      |
| test_trapeze_zero_perimeter            | a = 5, b = 0, c = 6, d = 4         | 0                   | Failed                      |
| text_trapeze_mul_digit_area            | a = 23, b = 12, h = 11             | 192.5               | Passed                      |
| test_trapeze_mul_digit_perimeter       | a = 23, b = 71, c = 55, d = 62     | 211                 | Passed                      |
| test_trapeze_single_digit_area         | a = 2, b = 6, h = 3                | 12                  | Passed                      |
| test_trapeze_single_digit_perimeter    | a = 2, b = 7, c = 5, d = 8         | 22                  | Passed                      |
| test_trapeze_fraction_area             | a = 5.25, b = 6, h = 4.2           | 23.625              | Passed                      |
| test_trapeze_fraction_perimeter        | a = 2.4, b = 7.5, c = 5, d = 8.4   | 23.3                | Passed                      |
| test_trapeze_negative_digit_area       | a = -5, b = 3, h = 2               | 0                   | Failed                      |
| test_trapeze_negative_digit_perimeter  | a = -2, b = 7, c = 6, d = 8        | 0                   | Failed                      |
| test_trapeze_string_area               | a = "5", b = "6", h = "4"          | 22                  | Failed                      |
| test_trapeze_string_perimeter          | a = "2", b = "7", c = "5", d = "8" | 22                  | Failed                      |
