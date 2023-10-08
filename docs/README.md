# Math formulas
## Area

- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Program description

The program is a set of functions for working with geometric shapes. The functions calculate geometric quantities (area and perimeter) for shapes (circle, rectangle, square and triangle), taking the required quantities as input.

# Program functions

## Circle

### Area
```python
def area(r)
```
Takes the radius of a circle and returns the area of the circle.

**Input** `3` -> **Output** `28.274333882308138`

### Perimeter
```python
def perimeter(r)
```
Takes the radius of a circle and returns the perimeter of the circle.

**Input** `5` -> **Output** `31.41592653589793`

## Rectangle

### Area
```python
def area(a, b)
```
Takes the sides of a rectangle and returns the area of the rectangle.

**Input** `3, 6` -> **Output** `18`

### Perimeter
```python
def perimeter(a, b)
```
Takes the sides of a rectangle and returns the perimeter of the rectangle.

**Input** `8, 5` -> **Output** `26`

## Square

### Area
```python
def area(a)
```
Takes the side of a square and returns the area of the square.

**Input** `5` -> **Output** `25`

### Perimeter
```python
def perimeter(a)
```
Takes the side of a square and returns the perimeter of the square.

**Input** `9` -> **Output** `36`

## Triangle

### Area
```python
def area(a, h)
```
Takes a side and the altitude of a triangle drawn to it and returns the area of the triangle.

**Input** `3, 7` -> **Output** `10.5`

### Perimeter
```python
def perimeter(a, b, c)
```
Takes three sides of a triangle and returns the perimeter of the triangle.

**Input** `1, 4, 3` -> **Output** `8`


# Change history

- `1d4754b` Fix bug in rectangle.py
- `ecd8078` Add new file rectangle.py
- `d078c8d` L-03: Docs added
- `8ba9aeb` Circle and square added

