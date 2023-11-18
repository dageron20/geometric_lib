# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Functions
### triangle.py
- **area(a, h)**
Принимает a (int) - длину стороны и h (int) - высоты треугольника
Возвращает площадь этого треугольника (int)
```python
print(area(3, 5))
```
<< 15

- **perimeter(a, b, c)**
Принимает длины трёх сторон треугольника a, b, c (int)
Возвращает периметр этого треугольника (int)
```python
print(perimeter(2, 3, 5))
```
  << 10
### rectangle.py
- **area(a, b)**
Принимает a, b (int) - длины сторон прямоугольника
Возвращает площадь этого прямоугольника
```python
print(area(7, 8))
```
<< 56

- **perimeter(a, b)**
Принимает a, b (int) - длины сторон прямоугольника
Возвращает периметр этого прямоугольника (int)
```python
print(peremeter(20, 5))
```
<< 50

### circle.py
- **area(r)**
Принимает r - длину радиуса окружности (int)
Возвращает площадь этой окружности (int)
```python
print(area(7))
```
<< 153.93804002589985

- **perimeter(r)**
Принимает r - длину радиуса окружности (int)
Возвращает периметр этой окружности (int)
```python
print(perimeter(8))
```
<< 50.26548245743669

### square.py
- **area(a)**
Принимает a - длину стороны квадрата (int)
Возвращает площадь этого квадрата (int)
```python
print(area(3))
```
<< 9

- **perimeter(a)**
Принимает a - длину стороны квадрата (int)
Возвращает периметр этого квадрата (int)
```python
print(perimeter(5))
```
<< 20

# UNIT-tests

## circle.py
| Test name | Input | Expected | Result | Status|
| --- | --- | --- | --- | --- |
| test_circle_area_regular | 2 | 12.566 | 12.566 | Ok
| test_circle_area_zero | 0 | ValueError | ValueError | Ok
| test_circle_area_negative | -2 | ValueError | ValueError | Ok
| test_circle_perimeter_regular | 3 | 18.85 | 18.85 | Ok
| test_circle_perimeter_zero | 0 | ValueError | ValueError | Ok
| test_circle_perimeter_negative | -3 | ValueError | ValueError | Ok

## rectangle.py
| Test name | Input | Expected | Result | Status|
| --- | --- | --- | --- | --- |
| test_rectangle_area_regular | 2, 3 | 6 | 6 | Ok
| test_rectangle_area_zero | 0, 32 | ValueError | ValueError | Ok
| test_rectangle_area_negative | -2, 2 | ValueError | ValueError | Ok
| test_rectangle_perimeter_regular | 4, 5 | 18 | 18 | Ok
| test_rectangle_perimeter_zero | 0, 5 | ValueError | ValueError | Ok
| test_rectangle_perimeter_negative | -1, 3 | ValueError | ValueError | Ok

## square.py
| Test name | Input | Expected | Result | Status|
| --- | --- | --- | --- | --- |
| test_square_area_regular | 4 | 16 | 16 | Ok
| test_square_area_zero | 0 | ValueError | ValueError | Ok
| test_square_area_negative | -2 | ValueError | ValueError | Ok
| test_square_perimeter_regular | 5 | 20 | 20 | Ok
| test_square_perimeter_zero | 0 | ValueError | ValueError | Ok
| test_square_perimeter_negative | -1 | ValueError | ValueError | Ok

## triangle.py
| Test name | Input | Expected | Result | Status|
| --- | --- | --- | --- | --- |
| test_triangle_area_regular | 3, 5 | 7.5 | 7.5 | Ok
| test_triangle_area_zero | 0, 56 | ValueError | ValueError | Ok
| test_triangle_area_negative | -3, 9 | ValueError | ValueError | Ok
| test_triangle_perimeter_regular | 6, 5, 8 | 19 | 19 | Ok
| test_triangle_perimeter_sides | 1, 4, 15 | ValueError | ValueError | Ok
| test_triangle_perimeter_zero | 0, 4, 7 | ValueError | ValueError | Ok
| test_triangle_perimeter_negative | -2, -5, 2 | ValueError | ValueError | Ok

# История изменения
- 680e1420db4d3c747d0ad593b3219bd02dd0ce4c - Kovrik Alexandr 6.10.2023
added documentation to functions
- 1dc1aeb842288847f492323f1d0d804ad0ad6886 - Kovrik Alexandr 25.09.2023
added triangle.py fixed rectangle.py
- 308c08897a53d95b898044e0a26c3d4cb760bc84 - Kovrik Alexandr 25.09.2023
added rectangle.py