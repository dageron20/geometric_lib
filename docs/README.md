# Mathematical formulas
## Area
- Circle: S = πR2
- Rectangle: S = ab
- Square: S = a2
- Triangle: S = ah / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c
<br/><br/>

# Project content
## Files in project:
- circle.py
- rectangle.py
- triangle.py
- square.py

Below are the ways to work with these files and the functions they contain.

## File circle.py
Contains two functions:

1. **def area(r)** - takes the number r - the radius of the circle, returns the area of the circle

*Example call:*  

```python
from circle import area
circleArea = area(3)
print(circleArea)
```
```
Result: 28.274333882308138
```
2. **def perimiter(r)** - takes the number r - the radius of the circle, returns the perimeter (length) of the circle

*Example call:*
```python
from circle import perimeter
circlePerimeter = perimeter(3)
print(circlePerimeter) 
```
```
Result: 18.84955592153876
```

## File rectangle.py
Contains two functions:

1. **def area(a, b)** - takes the numbers a, b - sides of the rectangle, returns the area of the rectangle

*Example call:*

```python
from rectangle import area
rectangleArea = area(2, 4)
print(rectangleArea)
```
```
Result: 8
```
2. **def perimiter(a,b)** - takes the numbers a, b - sides of the rectangle, returns the perimeter of the rectangle

*Example call:*
```python
from rectangle import perimeter
circlePerimeter = perimeter(2, 5)
print(circlePerimeter) 
```
```
Result: 14
```

## File square.py
Contains two functions:

1. **def area(a)** - takes the number a - side of the square, returns the square area  

*Example call:*

```python
from square import area
squareArea = area(4)
print(squareArea)
```
```
Result: 16
```
2. **def perimiter(a)** - takes the number a - side of the square, returns the perimeter of the square

*Example call:*
```python
from square import perimeter
squarePerimeter = perimeter(5)
print(squarePerimeter) 
```
```
Result: 20
```

## File triangle.py
Contains two functions:

1. **def area(a, h)** - accepts two numbers: a is the side of the triangle, the number h is the height lowered to the side a. Returns the area of the triangle

*Example call:*

```python
from triangle import area
triangleArea = area(2, 5)
print(triangleArea) 
```
```
Result: 5
```
2. **def perimiter(a, b, c)** - Takes the numbers a, b and c - sides of the triangle, returns the perimeter of the triangle

*Example call:*
```python
from triangle import perimeter
trianglePerimeter = perimeter(2, 3, 4)
print(trianglePerimeter) 
```
```
Result: 9
```

<br/>

# Unit tests

## TriangleTestCase.py
| Test name                        | Test description              | Input data       | Output         | Result |
|----------------------------------|-------------------------------|------------------|----------------|--------|
| testAreaCalcualtion()            | Normal value check            | 10, 5            | 25             | Pass
| testPerimeterCalcualtion()       | Normal value check            | 9, 7, 4          | 20             | Pass
| testAreaFloat()                  | Float value check             | 10.5, 2.5        | 13.125         | Pass
| testPerimeterFloat()             | Float value check             | 5.5, 5.5, 5.5    | 16.5           | Pass
| testAreaStr()                    | Str value check               | 'xyz', 'z'       | error          | Pass
| testPerimeterStr()               | Str value check               | 'xyz', 'x', 'z'  | error          | Pass
| testAreaNegative()               | Negative value check          | 9, -7            | -31.5          | Fail(expected error rise)
| testPerimeterNegative()          | Negative value check          | -10, -5, 6       | -9             | Fail(expected error rise)
| testPerimeterIncorrectTriangle() | Invalid triangle sides check  | 22, 4, 3         | 29             | Fail(expected error rise)

## RectangleTestCase.py
| Test name                        | Test description              | Input data       | Output         | Result |
|----------------------------------|-------------------------------|------------------|----------------|--------|
| testAreaCalcualtion()            | Normal value check            | 5, 10            | 50             | Pass
| testPerimeterCalcualtion()       | Normal value check            | 5, 10            | 30             | Pass
| testAreaFloat()                  | Float value check             | 5.5              | 30.25          | Pass
| testPerimeterFloat()             | Float value check             | 5.5              | 22             | Pass
| testAreaStr()                    | Str value check               | 'xyz', 'z'       | error          | Pass
| testPerimeterStr()               | Str value check               | 'xyz', 'q'       | error          | Pass
| testAreaNegative()               | Negative value check          | -10, -5          | 50             | Fail(expected error rise)
| testPerimeterNegative()          | Negative value check          | -10, -5          | -30            | Fail(expected error rise)

## CircleTestCase.py
| Test name                        | Test description              | Input data       | Output         | Result |
|----------------------------------|-------------------------------|------------------|----------------|--------|
| testPerimeterCalcualtion()       | Normal value check            | 5                | 31.41...       | Pass   |
| testAreaCalcualtion()            | Normal value check            | 5                | 78.53...       | Pass   |    
| testAreaFloat()                  | Float value check             | 5.5              | 95.03...       | Pass   |
| testPerimeterFloat()             | Float value check             | 5.5              | 34.55...       | Pass   |
| testAreaStr()                    | Str value check               | 'xyz'            | error          | Pass
| testPerimeterStr()               | Str value check               | 'xyz'            | error          | Pass
| testAreaNegative()               | Negative value check          | -10              | 314.15...      | Fail(expected error rise)|
| testPerimeterNegative()          | Negative value check          | -10              | -62.83...      | Fail(expected error rise)|

## SquareTestCase.py
| Test name                        | Test description              | Input data       | Output         | Result |
|----------------------------------|-------------------------------|------------------|----------------|--------|
| testAreaCalcualtion()            | Normal value check            | 5                | 25             | Pass
| testPerimeterCalcualtion()       | Normal value check            | 5                | 20             | Pass
| testAreaFloat()                  | Float value check             | 5.5              | 30.25          | Pass
| testPerimeterFloat()             | Float value check             | 5.5              | 22             | Pass
| testAreaStr()                    | Str value check               | 'xyz'            | error          | Pass
| testPerimeterStr()               | Str value check               | 'xyz'            | error          | Pass
| testAreaNegative()               | Negative value check          | -10              | 100            | Fail(expected error rise)
| testPerimeterNegative()          | Negative value check          | -10              | -40            | Fail(expected error rise)


# Project change history
| Commit | Author | Hash |
| --- | --- | --- |
| L-03: Circle and square added | smartiqa | [8ba9aeb](https://github.com/Tiipok/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460 ) |
| L-03: Docs added | smartiqa | [d078c8d](https://github.com/Tiipok/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2) |
| added rectangle.py | Tiipok | [817fdfe](https://github.com/Tiipok/geometric_lib/commit/817fdfe3e0c73271e14191f7debbaed9a436f390) |
| added triangle.py + fixed rectangle's perimeter calculations | Tiipok | [07ca407](https://github.com/Tiipok/geometric_lib/commit/07ca4073bc41cdb7ff15929090f05f99d420965d) |
| unit tests added | Tiipok | [bf3f111](https://github.com/Tiipok/geometric_lib/commit/bf3f1119e1a996a197eecd3dd6f3a8aac50d92c2) |