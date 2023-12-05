# Математические формулы
## Нахождение площади
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Нахождение периметра
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Функции
## Круг
### Вычисление площади
*(r - радиус)*
```python
def area(r):
```
> Пример вызова: area(5) -> 78.53981633974483

### Вычисление периметра
*(r - радиус)*
```python
def perimeter(r):
```
> Пример вызова: perimeter(5) -> 31.41592653589793

## Прямоугольник
### Вычисление площади
*(a,b - стороны прямоугольника)*
```python
def area(a, b):
```
> Пример вызова: area(3, 4) -> 12

### Вычисление периметра
*(a,b - стороны прямоугольника)*
```python
def perimeter(a, b):
```
> Пример вызова: perimeter(3, 4) -> 14

## Квадрат
### Вычисление площади
*(a - сторона квадрата)*
```python
def area(a):
```
> Пример вызова: area(3) -> 9

### Вычисление периметра
*(a - сторона квадрата)*
```python
def perimeter(a):
```
> Пример вызова: perimeter(3) -> 12

## Треугольник
### Вычисление площади
*(a - основание, h - высота)*
```python
def area(a, h):
```
> Пример вызова: area(3, 4) -> 6

### Вычисление периметра
*(a,b,c - стороны треугольника)*
```python
def perimeter(a, b, c):
```
> Пример вызова: perimeter(3, 4, 5) -> 12


# Unit Tests

## circle.py
| Test name | Function | Input | Expected | Status |
| --- | --- | --- | --- | --- |
| test_circle_int_first | area | 5 | 78.53981633974483 | OK
| | perimeter | 7 | 43.982297150257104 | OK
| test_circle_string_first | area | "ITMO" | "Аргумент должен быть int" | FAILED
| | perimeter | "M3108" | "Аргумент должен быть int" | FAILED
| test_circle_negative_int_first | area | -5 | "Аргумент должен быть больше ноля" | FAILED
| | perimeter | -7 | "Аргумент должен быть больше ноля" | FAILED
| test_circle_zero | area | 0 | "Аргумент должен быть больше ноля" | FAILED
|| perimeter | 0 | "Аргумент должен быть больше ноля" | FAILED

## rectangle.py
| Test name | Function | Input | Expected | Status |
| --- | --- | --- | --- | --- |
| test_rectangle_int_first | area | 5, 19 | 95 | OK
| | perimeter | 5, 9 | 28 | OK
| test_rectangle_string_first | area | "ITMO" | "Аргументы должен быть int" | FAILED
| | perimeter | "M3108" | "Аргументы должен быть int" | FAILED
| test_rectangle_negative_int_first | area | -5 | "Аргументы должны быть больше ноля" | FAILED
| | perimeter | -7 | "Аргументы должны быть больше ноля" | FAILED
| test_rectangle_zero | area | 0 | "Аргументы должны быть больше ноля" | FAILED
|| perimeter | 0 | "Аргументы должны быть больше ноля" | FAILED

## square.py
| Test name | Function | Input | Expected | Status |
| --- | --- | --- | --- | --- |
| test_square_int_first | area | 5 | 25 | OK
| | perimeter | 7 | 28 | OK
| test_square_string_first | area | "ITMO" | "Аргумент должен быть int" | FAILED
| | perimeter | "M3108" | "Аргумент должен быть int" | FAILED
| test_square_negative_int_first | area | -5 | "Аргумент должен быть больше ноля" | FAILED
| | perimeter | -7 | "Аргумент должен быть больше ноля" | FAILED
| test_square_zero | area | 0 | "Аргумент должен быть больше ноля" | FAILED
|| perimeter | 0 | "Аргумент должен быть больше ноля" | FAILED

## triangle.py
| Test name | Function | Input | Expected | Status |
| --- | --- | --- | --- | --- |
| test_triangle_int_first | area | 5, 8 | 20 | OK
| | perimeter | 5, 8, 2 | 15 | OK
| test_triangle_string_first | area | "ITMO" | "Аргументы должен быть int" | FAILED
| | perimeter | "M3108" | "Аргументы должен быть int" | FAILED
| test_triangle_negative_int_first | area | -5 | "Аргументы должны быть больше ноля" | FAILED
| | perimeter | -7 | "Аргументы должны быть больше ноля" | FAILED
| test_triangle_zero | area | 0 | "Аргументы должны быть больше ноля" | FAILED
|| perimeter | 0 | "Аргументы должны быть больше ноля" | FAILED

# Changelog
- [Fixed rectangle.py](https://github.com/soilow/geometric_lib/commit/68eb5b9fa84158b73667fd18002cd3c1c36a62bf)
- [Added triangle.py](https://github.com/soilow/geometric_lib/commit/0737645eb11b576050358c21c90d048ab8ff9a61)
- [Added rectangle.py](https://github.com/soilow/geometric_lib/commit/176e0720cda60b0d434ee8ba5a3a934610403548)
- [L-03: Docs added](https://github.com/soilow/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2)
- [L-03: Circle and square added](https://github.com/soilow/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460)

