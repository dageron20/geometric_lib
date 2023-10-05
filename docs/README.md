# General description of the solution
## Purpose
The solution is designed to calculate the area and perimeter of presented shapes:
+ circle.py - for circle
+ rectangle.py - for rectangle
+ square.py - for square
+ triangle.py - for triangle

## Structure
```
docs
  | -- README.md
circle.py
rectangle.py
square.py
triangle.py
```

# Usage
## circle.py
### area(r)
Calculating the area of the circle

Parameters:
+ r (int/float) - radius of the circle

Returns:
+ (float) - area of the circle

Usage:
```python
>>> area(5)
>>> 78.53981633974483
```

### perimeter(r)
Calculating the perimeter of the circle

Parameters:
+ r (int/float) - radius of the circle

Returns:
+ (float) - perimeter of the circle

Usage:
```python
>>> perimeter(5)
>>> 31.41592653589793
```

## rectangle.py
### area(a, b)
Calculating the area of the rectangle

Parameters:
+ a (int/float) - a side of the rectangle
+ b (int/float) - b side of the rectangle

Returns:
+ (int/float) - area of the rectangle

Usage:
```python
>>> area(5, 4)
>>> 20
```

### perimeter(a, b)
Calculating the perimeter of the rectangle

Parameters:
+ a (int/float) - a side of the rectangle
+ b (int/float) - b side of the rectangle

Returns:
+ (int/float) - perimeter of the rectangle

Usage:
```python
>>> perimeter(5, 4)
>>> 18
```

## square.py
### area(a)
Calculating the area of the square

Parameters:
+ a (int/float) - a side of the square

Returns:
+ (int/float) - area of the square

Usage:
```python
>>> area(5)
>>> 25
```

### perimeter(a)
Calculating the perimeter of the square

Parameters:
+ a (int/float) - a side of the square

Returns:
+ (int/float) - perimeter of the square

Usage:
```python
>>> perimeter(5)
>>> 20
```

## triangle.py
### area(a, h)
Calculating the area of the triangle

Parameters:
+ a (int/float) - side of the triangle
+ h (int/float) - height of the triangle

Returns:
+ (int/float) - area of the triangle

Usage:
```python
>>> area(5, 3)
>>> 7.5
```

### perimeter(a, b, c)
Calculating the perimeter of the triangle

Parameters:
+ a (int/float) - a side of the triangle
+ c (int/float) - b side of the triangle
+ b (int/float) - c side of the triangle

Returns:
+ (int/float) - perimeter of the triangle

Usage:
```python
>>> perimeter(5, 3, 2)
>>> 10
```

# Changelog
## Docs

Commit: 783a968f2cbe24b51d3ae3922fbc9155abeaff91

Date: 05.10.2023

Usage blocks added in function comments

## Docs

Commit: 7a898d0fcf21d1d9f2beced3d068b316678633e1

Date: 05.10.2023

README.md expanded, added sections

## Docs

Commit: 55490b6585037028de5adc5b9f1019a36b5ec5ef

Date: 05.10.2023

Added comments to functions

## Rectangle fix

Commit: 376867b12a6d15738f191d1b9b4fdcb53fa9b4d4

Date: 21.09.2023

Fixed a mistake in calculating the perimeter of a rectangle

## Rectangle

Commit: 894c52f4156d5573dd497b8fac7fa0d70d9181f1

Date: 21.09.2023

Added module for calculating the area and perimeter for a rectangle

## Docs

Commit: d078c8d9ee6155f3cb0e577d28d337b791de28e2

Date: 04.04.2023

Added docs: README.md

## Circle and Square

Commit: 8ba9aeb3cea847b63a91ac378a2a6db758682460

Date: 04.04.2023

Added modules for calculating the area and perimeter for a circle and a square

# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
