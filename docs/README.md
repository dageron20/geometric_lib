# Общее описание решения 
Проект считает площади и перимерты следующих фигур: 
- круга
- квадрата
- прямоугольника
- треугольника

# Описание функциий
## circle.py:
- def area(r):

     Принимает число r - радиус круга, возвращает его площадь (π*r^2)

- def perimeter(r):

     Принимает числе r - радиус круга, возвращает его периметр (2*π*r)
  
## rectangle.py:
- def area(a, b):

     Принимает числа a и b - стороны прямоугольника, возвращает его площадь (a*b)

- def perimeter(a, b):

     Принимает числа a и b - стороны прямоугольника, возвращает его периметр (2(a+b))

## square.py:
- def area(a):

     Принимает число a - сторону квадрата, возвращает его площадь (a^2)

- def perimeter(a):

     Принимает числе a - сторону квадрата, возвращает его периметр (4*a)

## triangle.py:
- def area(a, h):

     Принимает числа a и h - сторону треугольника и опущенную на неё высоту, возвращает его площадь (a*h/2)

- def perimeter(a, b, c):

     Принимает числа a, b и c - стороны треугольника, возвращает его периметр (a+b+c)

# UNIT-tests

## circle.py
| Test name | function | Input | Expected | Status|
| --- | --- | --- | --- | --- |
| test_integer_or_float | area | 3 | 28.274333882308138 | OK
| | perimeter | 5.4 | 33.929200658769766 | OK
| test_negative_and_zero | area | 0 | "radius cannot be zero" | FAILED
| | perimeter | -7 | "radius cannot be negative" | FAILED
| test_not_integer_or_float_type | area | True | "radius must be integer or float values" | FAILED
| | perimeter | "6" | "radius must be integer or float values" | FAILED

## rectangle.py
| Test name | function | Input | Expected | Status|
| --- | --- | --- | --- | --- |
| test_integer_or_float | area | 5.9, 15 | 88.5 | OK
| | perimeter | 9, 6.1 | 30.2 | OK
| test_negative_and_zero | area | -15, 0 | "sides of rectangle must be natural" | FAILED
| | perimeter | 9, -47 | "sides of rectangle must be natural" | FAILED
| test_not_integer_or_float_type | area | [5, 7], True | "sides of rectangle must be integer or float values" | FAILED
| | perimeter | "8", {0} | "sides of rectangle must be integer or float values" | FAILED

## square.py
| Test name | function | Input | Expected | Status|
| --- | --- | --- | --- | --- |
| test_integer_or_float | area | 7.5 | 56.25 | OK
| | perimeter | 15 | 60 | OK
| test_negative_and_zero | area | -16 | "sides of square must be natural" | FAILED
| | perimeter | 0 | "sides of square must be natural" | FAILED
| test_not_integer_or_float_type | area | [5] | "sides of square must be integer or float values" | FAILED
| | perimeter | {10} | "sides of square must be integer or float values" | FAILED

## triangle.py
| Test name | function | Input | Expected | Status|
| --- | --- | --- | --- | --- |
| test_integer_or_float | area | 5.9, 15 | 44.25 | OK
| | perimeter | 5, 4.23, 3 | 12.23 | OK
| test_negative_and_zero | area | 0, -7 | "sides and height of triangle must be natural" | FAILED
| | perimeter | -10, 0, 16.8 | "sides of triangle must be natural" | FAILED
| test_not_integer_or_float_type | area | '5', "12" | "sides and height of triangle must be integer or float values" | FAILED
| | perimeter | {9}, False, 1 | "sides of triangle must be integer or float values" | FAILED
| test_triangle_exist | perimeter | 5, 15, 2 | "triangle doesn't exist" | FAILED

# История изменения проекта
- L-03: Circle and square added -- 8ba9aeb3cea847b63a91ac378a2a6db758682460
- L-03: Docs added -- d078c8d9ee6155f3cb0e577d28d337b791de28e2
- Add new file -- a2a132118c6fde3c4173125389a6754e06cf9e0e
- Fix error -- dec19a5e21efd5da7a2079499733b4c4a4122ffd
