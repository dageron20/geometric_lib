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

The program is a set of functions for working with geometric shapes. The functions calculate geometric quantities (area
and perimeter) for shapes (circle, rectangle, square and triangle), taking the required quantities as input.

# Program functions

## Circle

### Area

```python
def area(r)
```

Takes the radius of a circle and returns the area of the circle.

**Input** `area(3)` -> **Output** `28.274333882308138`

### Perimeter

```python
def perimeter(r)
```

Takes the radius of a circle and returns the perimeter of the circle.

**Input** `perimeter(5)` -> **Output** `31.41592653589793`

## Rectangle

### Area

```python
def area(a, b)
```

Takes the sides of a rectangle and returns the area of the rectangle.

**Input** `area(3, 6)` -> **Output** `18`

### Perimeter

```python
def perimeter(a, b)
```

Takes the sides of a rectangle and returns the perimeter of the rectangle.

**Input** `perimeter(8, 5)` -> **Output** `26`

## Square

### Area

```python
def area(a)
```

Takes the side of a square and returns the area of the square.

**Input** `area(5)` -> **Output** `25`

### Perimeter

```python
def perimeter(a)
```

Takes the side of a square and returns the perimeter of the square.

**Input** `perimeter(9)` -> **Output** `36`

## Triangle

### Area

```python
def area(a, h)
```

Takes a side and the altitude of a triangle drawn to it and returns the area of the triangle.

**Input** `area(3, 7)` -> **Output** `10.5`

### Perimeter

```python
def perimeter(a, b, c)
```

Takes three sides of a triangle and returns the perimeter of the triangle.

**Input** `perimeter(1, 4, 3)` -> **Output** `8`

# Unit tests

## circle.py

| Name                    | Input  | Result            | Expected result   | Status |
|-------------------------|--------|-------------------|-------------------|--------|
| test_area_zero          | r = 0  | 0                 | 0                 | OK     |
| test_area_regular       | r = 4  | 50.26548245743669 | 50.26548245743669 | OK     |
| test_area_negative      | r = -3 | ValueError        | ValueError        | OK     |
| test_perimeter_zero     | r = 0  | 0                 | 0                 | OK     |
| test_perimeter_regular  | r = 5  | 31.41592653589793 | 31.41592653589793 | OK     |
| test_perimeter_negative | r = -8 | ValueError        | ValueError        | OK     |

## rectangle.py

| Name                    | Input         | Result     | Expected result | Status |
|-------------------------|---------------|------------|-----------------|--------|
| test_area_zero          | a = 0, b = 2  | 0          | 0               | OK     |
| test_area_regular       | a = 2, b = 4  | 8          | 8               | OK     |
| test_area_negative      | a = 8, b = -5 | ValueError | ValueError      | OK     |
| test_perimeter_zero     | a = 0, b = 0  | 0          | 0               | OK     |
| test_perimeter_regular  | a = 3, b = 1  | 8          | 8               | OK     |
| test_perimeter_negative | a = -8, b = 3 | ValueError | ValueError      | OK     |

## square.py

| Name                    | Input  | Result     | Expected result | Status |
|-------------------------|--------|------------|-----------------|--------|
| test_area_zero          | a = 0  | 0          | 0               | OK     |
| test_area_regular       | a = 2  | 4          | 4               | OK     |
| test_area_negative      | a = -1 | ValueError | ValueError      | OK     |
| test_perimeter_zero     | a = 0  | 0          | 0               | OK     |
| test_perimeter_regular  | a = 3  | 12         | 12              | OK     |
| test_perimeter_negative | a = -8 | ValueError | ValueError      | OK     |

## triangle.py

| Name                    | Input                 | Result     | Expected result | Status |
|-------------------------|-----------------------|------------|-----------------|--------|
| test_area_zero          | a = 5, h = 0          | 0          | 0               | OK     |
| test_area_regular       | a = 1, h = 3          | 1.5        | 1.5             | OK     |
| test_area_negative      | a = -1, h = 8         | ValueError | ValueError      | OK     |
| test_perimeter_zero     | a = 0, b = 0, c = 0   | 0          | 0               | OK     |
| test_perimeter_regular  | a = 8, b = 1, c = 9   | 18         | 18              | OK     |
| test_perimeter_negative | a = -8, b = 3, c = -5 | ValueError | ValueError      | OK     |

# Change history

- `1d4754b` Fix bug in rectangle.py
- `ecd8078` Add new file rectangle.py
- `d078c8d` L-03: Docs added
- `8ba9aeb` Circle and square added

