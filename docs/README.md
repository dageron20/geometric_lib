# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Description of solution:
## Made functions to find the area and perimeter of shapes: circle, rectangle, square, triangle

# Description of functions:
## Circle:
```python
import math

def area(r):
return math.pi * r * r

def perimetr(r):
return 2 * math.pi * r
```
- File code circle.py

```python
def area(r):
	return math.pi * r * r
```
- The function for calculating the area takes the number **r** - the radius of the circle for further calculation of the area of ​​the circle

```python
def perimetr(r):
	return 2 * math.pi * r
```

- The function for calculating the perimeter of a circle takes the number **r** - the radius of the circle to calculate the perimeter of the circle

### Example call:
```python
import math

def area(r):
    return math.pi * r * r

def perimetr(r):
    return 2 * math.pi * r

print(area(5))
print(perimeter(5))
```

- Result area function = 78.53981633974483
- Result perimeter function = 31.41592653589793

## Rectangle
```python
def area(a, b):
    return a * b

def perimetr(a, b):
    return 2 * (a + b)
```

- File code rectangle.py

```python
def area(a, b):
	return a * b
```
- Takes two numbers: a and b - the length and width of the rectangle to calculate its area

```python
def perimetr(a, b):
	return 2 * (a + b)
```
- The function for calculating the perimeter takes two numbers: a and b - the length and width of the rectangle to calculate its perimeter
### Example call:
```python
def area(a, b):
    return a * b

def perimetr(a, b):
    return 2 * (a + b)

print(area(2, 4))
print(perimetr(2, 4))
```

- Result area function = 8
- Result perimetr function = 12

## Square
```python
def area(a):
    return a * a

def perimetr(a):
    return 4 * a
```
- File code square.py

```python
def area(a):
	return a * a
```
- The function for calculating the area takes the number a - the side of the square to calculate its area


```python
def perimetr(a):
	return 4 * a
```
- The function for calculating the perimeter takes the number a - the side of the square to calculate its perimeter
### Example call:
```python
def area(a):
    return a * a

def perimetr(a):
    return 4 * a

print(area(6))
print(perimetr(6))
```
- Result area function = 36
- Result perimeter function 24
## Triangle
```python
def area(a, h):
    return a * h / 2

def perimetr(a, b, c):
    return a + b + c
```
- File code tiangle.py

```python
def area(a, h):
	return a * h / 2
```
- The function for calculating the area takes two numbers: a and h - the side and height of the triangle to calculate its area
```python

def perimetr(a, b, c):
	return a + b + c
```
- The function for calculating the perimeter takes three numbers: a, b, c - sides of the triangle

### Example call:
```python
def area(a, h):
    return a * h / 2

def perimetr(a, b, c):
    return a + b + c


print(area(2, 4))
print(perimetr(2, 3, 4))
```
- Result area function = 4
- Result perimeter function = 9
# Project change history with commit hashes
> commit 895de6d4ac25263a47e41d7919260685826c7e5b (HEAD -> main, origin/main, origin/HEAD)
- | Author: Taras <nebarrow@yandex.ru>
- | Date:   Mon Sep 18 19:12:37 2023 +0300
- |
- |     была исправлена ошибка в вычислении периметра прямоугольника в файле rectangle.py.


> commit b441342a4b0460f0e1c6895932e64ee43f4d07c5
- | Author: Taras <nebarrow@yandex.ru>
- | Date:   Mon Sep 18 19:08:11 2023 +0300
- |
- |     был добавлен новый файл rectangle.py с вычислениями для фигуры Прямоугольник


> commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
-  | Author: smartiqa <info@smartiqa.ru>
-  | Date:   Thu Mar 4 14:55:29 2021 +0300
-  |
-  |     L-03: Docs added