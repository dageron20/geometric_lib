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
> commit 2ece1a3e14338db587397651f785c5c348ea4248
- | Author: Maxim <karimovmaksim121@gmail.com>
- | Date:   Wed Oct 4 20:45:56 2023 +0500
- |
- | ADD: rectangle.py

> commit 5f79b2c971f70f66fa2594759e236839c84bc683 (HEAD -> main, origin/main, origin/HEAD)
- | Author: Maxim <karimovmaksim121@gmail.com>
- | Date:   Wed Oct 4 20:47:36 2023 +0500
- |
- | ADD triangle.py; FIX: rectangle.py
