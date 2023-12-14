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
<<<<<<< HEAD

### Unit Tests
- File code tests.py
```python
import unittest
import math

import rectangle
import square
import triangle
import circle

class BaseTestCase(object):
    def test_perimeter(self):
        for inp, outp in self.perimeter_testcases:
            result = self.module.perimeter(*inp)
            self.assertEqual(result, outp, f'{self.module.__name__}:perimeter\t{inp=} expected={outp} returned={result}')
            
    def test_area(self):
        for inp, outp in self.area_testcases:
            result = self.module.area(*inp)
            self.assertEqual(result, outp, f'{self.module.__name__}:area\t{inp=} expected={outp} returned={result}')
            
    
class RectangleTest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        self.module = rectangle
        self.area_testcases = (
            ((0, 0), 0),
						((5, 0), 0),
            ((0, 'a'), KeyError),
            ((3, -3), KeyError),
            ((5, 5), 25),
        )
        self.perimeter_testcases = (
            ((0, 0), 0),
            ((5, 'a'), KeyError),
            ((-10, 0), KeyError),
            ((0, 10), 20),
            ((10, -10), KeyError),
        )

class SquareTest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        self.module = square
        self.area_testcases = (
            ((10, ), 100),
            (('a', ), KeyError),
            ((-1, ), KeyError),
            ((1.5, ), 2.25),
            ((12, ), 144),
        )
        self.perimeter_testcases = (
            ((0, ), 0),
            ((1, ), 4),
            ((-2, ), KeyError),
            ((100, ), 400),
            ((15, ), 60),
        )

class TriangleTest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        self.module = triangle
        self.area_testcases = (
            ((0, 123), 0),
            ((0, 2), 0),
            ((5, 0), 0),
            ((999999999999, 0), 0),
            ((5, -3), KeyError),
        )
        self.perimeter_testcases = (
            ((0, 0, 0), 0),
            ((0, 0, 1), KeyError),
            ((0, 1, 0), KeyError),
            ((1, 0, 0), KeyError),
            ((1, 0, -1), KeyError)
        )

class CircleTest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        self.module = circle
        self.area_testcases = (
            ((0, ), 0),
            ((1, ), math.pi),
            ((2, ), math.pi * 4),
            ((0.5, ), math.pi * 0.25),
        )
        self.perimeter_testcases = (
            ((0, ), 0),
            ((1, ), math.pi * 2),
            ((2, ), math.pi * 4),
            ((3, ), math.pi * 6),
            ((10, ), math.pi * 20),
            ((100, ), math.pi * 200),
            ((0.5, ), math.pi),
            ((1.3, ), math.pi * 2.6),
        )
```

-  class BaseTestCase(object): base class for several functions to test the product and reduce the amount of code
- Next are 4 classes for module checks, which are inherited from the base class and from the built-in library Unit tests in python
- Each of which checks against a set of input data

- test list [File](https://github.com/mak7im-05/geometric_lib/blob/main/%D0%BE%D1%82%D1%87%D0%B5%D1%82%20%D0%BF%D0%BE%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E.pdf)



## Project change history with commit hashes
> commit 54029aef4b78f8468b63d7ed1cdc136a86b03afa (HEAD -> main, origin/main, origin/HEAD)
- | Author: Maxim <karimovmaksim121@gmail.com>
- | Date:   Wed Sep 13 19:34:15 2023 +0500
- |
- |     FIX: rectangle.py


> commit d93c047818ab0a08f8978e1700e0f884e1ee7dc8
- | Author: Maxim <karimovmaksim121@gmail.com>
- | Date:   Wed Sep 13 19:29:51 2023 +0500
- |
- |     FIX: rectangle.py; ADD: triangle.py


> commit e802e55f4c24cbfce3026419972cb13f0e6c14fb
-  | Author: Maxim <karimovmaksim121@gmail.com>
-  | Wed Sep 13 19:22:28 2023 +0500
-  |
-  |     ADD: rectangle.py

> commit e802e55f4c24cbfce3026419972cb13f0e6c14fb
-  | Author: Maxim <karimovmaksim121@gmail.com>
-  | Wed Sep 13 19:22:28 2023 +0500
-  |
-  |     CHANGE: README.md

> commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
- | Author: smartiqa <info@smartiqa.ru>
- | Date:   Thu Mar 4 14:55:29 2021 +0300
- |
- |    L-03: Docs added
=======
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
>>>>>>> 532f9ecd9dd7a08e0e9ca867044f1a13a00236ab
