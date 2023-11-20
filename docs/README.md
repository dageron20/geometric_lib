# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a * h / 2
## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Functions
### Circle
```
area(r)
```
Gets a number r - radius of Circle. Returns circle area using formula _S = πR²_

```
perimeter(r)
```
Gets number r - radius of Circle. Returns circle perimiter using formula _P = 2πR_

### Rectangle
```
area(a, b)
```
Gets two numbers a, b - sides of rectangle. Returns rectangle area using formula _S = ab_
```
perimiter(a, b)
```
Gets two numbers a, b - sides of rectangle. Returns rectangle perimeter using formula _P = 2a + 2b_

### Square
```
area(a)
```
Gets number a - side of square. Returns Square area using formula _S = a²_
```
perimiter(a)
```
Gets number a - side of square. Returns Square perimiter using formula _P = 4a_

### Triangle
```
area(a, h)
```
Gets two numbers a and h - base and height of triangle. Returns its area using formula _S = a * h / 2_
```
perimiter(a, b, c)
```
Gets three numbers a, b, c - sides of triangle. Returns its perimeter using formula _P = a + b + c_

# Unit testing
This project has __tests.py__ file that contains unit test for __area__ and __perimeter__ functions of product's modules.

## Test functions
### Circle Test Case
- ```test_circle_zero_area```: Tests the ```area()``` function of the __circle__ module with a radius of 0 and verifies that the result is 0.
- ```test_circle_positive_area```: Tests the ```area()``` function of the __circle__ module with positive radius and verifies that the result is correct.
- ```test_circle_perimeter```: Tests the ```perimeter()``` function of the __circle__ module with different values of radius and verifies that the result is correct.

### Rectangle Test Case
- ```test_rectangle_zero_area```: Tests the ```area()``` function of the __rectangle__ module different cases when area should be 0 and verifies that the result is 0.
- ```test_rectangle_positive_area```: Tests the ```area()``` function of the __rectangle__ module with positive width and height and verifies that the result is correct.
- ```test_rectangle_perimeter```: Tests the ```perimeter()``` function of the __rectangle__ module with different values of width and height and verifies that the result is correct.

### Square Test Case
- ```test_square_zero_area```: Tests the ```area()``` function of the __square__ module with a side of 0 and verifies that the result is 0.
- ```test_square_positive_area```: Tests the ```area()``` function of the __square__ module with positive side and verifies that the result is correct.
- ```test_square_perimeter```: Tests the ```perimeter()``` function of the __square__ module with different values of side and verifies that the result is correct.

### Triangle Test Case
- ```test_triangle_zero_area```: Tests the ```area()``` function of the __triangle__ module with different cases when area should be 0 and verifies that the result is 0.
- ```test_triangle_positive_area```: Tests the ```area()``` function of the __triangle__ module with positive side and height values and verifies that the result is correct.
- ```test_triangle_perimeter```: Tests the ```perimeter()``` function of the __triangle__ module with different values of sides of triangles and verifies that the result is correct.
  
## Test cases

| Test name | Input | Expected output | Result |
| -------------- | -------------- | ------------------ | --------- |
| test_circle_zero_area | radius = 0 | 0 | True |
| test_circle_positive_area | radius = 23 | 1661 | True |
| test_circle_positive_area | radius = "23" | None | False |
| test_circle_positive_area | radius = True | None | False |
| test_circle_positive_area | radius = [] | None | False |
| test_circle_positive_area | radius = -10 | None | False |
| test_circle_perimeter | radius = 0 | 0 | True |
| test_circle_perimeter | radius = "23" | None | False |
| test_circle_perimeter | radius = True | None | False |
| test_circle_perimeter | radius = [] | None | False |
| test_circle_perimeter | radius = -10 | None | False |
| test_rectangle_zero_area | width = 5, height = 0| 0 | True |
| test_rectangle_positive_area |width = 23, height = 2 | 46 | True |
| test_rectangle_perimeter | width = 23, height = 12 | 70 | True |
| test_square_zero_area | side = 0 | 0 | True |
| test_square_positive_area | side = 5 | 25 | True |
| test_square_perimeter | side = 2 | 92 | True |
| test_triangle_zero_area | base = 0, height = 0 | 0 | True |
| test_triangle_positive_area | base = 2135, height = 242 | 258335 | True |
| test_triangle_perimeter | side1 = 2362, side2 = 3924, side3 = 8123 | 14409 | True |

## How to launch tests

To launch testing write command below to the shell:

```shell
python -m unittest tests.py
```
# Commit history
```
9a5259b Added comments with info about all funcs
8d82e0b Small fix
eb9990a Rectangle perimeter issue was solved
251e942 File ractangle.py has been added
d078c8d L-03: Docs added
8ba9aeb L-03: Circle and square added
b2403b0 Added unit tests
```
