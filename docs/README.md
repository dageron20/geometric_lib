# geometric_lib
**This project is designed to calculate the perimeter and area of the simplest geometric shapes**
## Shapes for which parameter counting is implemented
- Circle
- Rectangle
- Square
- Triangle
# Functions
## [circle.py](https://github.com/ArtemMoroz51/geometric_lib/blob/main/circle.py)
*This file is designed to calculate the area and perimeter of the circle.Contains the following functions:*
### `area(r)`
The function takes one `int` or `float` type argument - r, the radius of a given circle.\
The function returns one `float` type argument, the area of a given circle.\
Example of a call:\
`area(3)`\
returns: `28.274333882308138`
### `perimeter(r)`
The function takes one `int` or `float` type argument - r, the radius of a given circle.\
The function returns one `float` type argument, the perimeter of a given circle.\
Example of a call:\
`perimeter(3)`\
returns: `18.84955592153876`

## [rectangle.py](https://github.com/ArtemMoroz51/geometric_lib/blob/main/rectangle.py)
*This file is designed to calculate the area and perimeter of the rectangle.Contains the following functions:*
### `area(a, b)`
The function takes two `int` or `float` type argument - (a,b), sides of this rectangle.\
The function returns one `int` or `float` type argument, the area of a given rectangle.\
Example of a call:\
`area(3, 4)`\
returns: `12`
### `perimeter(a, b)`
The function takes two `int` or `float` type argument - (a,b), sides of this rectangle.\
The function returns one `int` or `float` type argument, the perimeter of a given rectangle.\
Example of a call:\
`perimeter(3, 4)`\
returns: `14`

## [square.py](https://github.com/ArtemMoroz51/geometric_lib/blob/main/square.py)
*This file is designed to calculate the area and perimeter of the square.Contains the following functions:*
### `area(a)`
The function takes one `int` or `float` type argument - a, side of this square.\
The function returns one `int` or `float` type argument, the area of a given square.\
Example of a call:\
`area(3)`\
returns: `9`
### `perimeter(a)`
The function takes one `int` or `float` type argument - a, side of this square.\
The function returns one `int` or `float` type argument, the perimeter of a given square.\
Example of a call:\
`perimeter(4)`\
returns: `16`

## [triangle.py](https://github.com/ArtemMoroz51/geometric_lib/blob/main/triangle.py)
*This file is designed to calculate the area and perimeter of the square.Contains the following functions:*
### `area(a)`
The function takes two `int` or `float` type argument:\
 a -  side of this triangle\
 h - the height drawn to this side\

The function returns one `int` or `float` type argument, the area of a given triangle.\
Example of a call:\
`area(3, 4)`\
returns: `6`
### `perimeter(a)`
The function takes three `int` or `float` type argument - a,b,c sides of this triangle.\
The function returns one `int` or `float` type argument, the perimeter of a given triangle.\
Example of a call:\
`perimeter(4, 5, 2)`\
returns: `11`

# Project change histoty
## commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
- **Author**: smartiqa <info@smartiqa.ru>
- **Date**:   Thu Mar 4 14:54:08 2021 +0300
- **Content**: L-03: Circle and square added

## commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
- **Author**: smartiqa <info@smartiqa.ru>
- **Date**:   Thu Mar 4 14:55:29 2021 +0300
- **Content**: Docs added

## commit 56f396facfc05ca81e958e5789303eb0cc4f0d4d
- **Author**: Artem <artemmoroz.w@gmail.com>
- **Date**:   Fri Sep 15 13:03:14 2023 +0300
- **Content**:  A new file has been added rectangle.py to calculate the area and perimeter of a rectangle

## commit  324d3a40df6f473285f75f44c2e5d0e8074f2011
- **Author**: Artem <artemmoroz.w@gmail.com>
- **Date**:   Fri Sep 15 13:17:34 2023 +0300
- **Content**:  Fixed a bug in calculating the perimeter of a rectangle

## commit  52042355a1fabc69967ba077463d78cb58a152db (HEAD -> main, origin/main, origin/HEAD)
- **Author**: Artem <artemmoroz.w@gmail.com>
- **Date**:   Fri Sep 15 15:33:28 2023 +0300
- **Content**:  Saving a file rectangle.py

## commit  d57e57f37d1a2cc0193f356b8e9c42a5ff827b4d (HEAD -> main, origin/main, origin/HEAD)
- **Author**: Artem <artemmoroz.w@gmail.com>
- **Date**:   Wed Oct 4 13:58:30 2023 +0300
- **Content**:  Labwork two
# Tests
To successfully pass all the tests, the program had to correctly calculate the areas and perimeters of various geometric shapes.\
The function should also work correctly for large numbers (long arithmetic), for fractional numbers, and take into account borderline cases when one of the elements of the function is zero.
- ### Tests for circle.py
| Name of the test        | Input data  | Result             |
|-------------------------|:-----------:|:-------------------|
| test_area_fraction      |   56.234    | 9934.541442970212  |
| test_circle_area_pi     |     pi      | 31.006276680299816 |
| test_circle_perimetr_pi |     pi      | 19.739208802178716 |
| test_perimetr_big_data  | 57512357891 | 361360802081.9851  |
- ### Tests for rectangle.py
| Name of the test                 |   Input data    | Result            |
|----------------------------------|:---------------:|:------------------|
| test_rectangle_area_double       |     10, 10      | 100               |
| test_rectangle_area_fraction     | 45.678, 21.5678 | 985.1739683999998 |
| test_rectangle_perimetr_fraction | 789.123, 11.146 | 1600.538          |
| test_perimetr_big_data           |      10, 0      | 20                |
### Tests for square.py
| Name of the test                  |     Input data     | Result                  |
|-----------------------------------|:------------------:|:------------------------|
| test_zero_area                    |         0          | 0                       |
| test_square_area_big_data         |    77634100891     | 6027053621153966993881  |
| test_square_perimetr_one          |         1          | 4                       |
| test_square_perimetr_big_data     | 457997155624564456 | 1831988622498257824     |
### Tests for triangle.py
| Name of the test                   |         Input data         | Result                 |
|------------------------------------|:--------------------------:|:-----------------------|
| test_zero_height_area              |            5, 0            | 0                      |
| test_triangle_area_big_data        | 9423847329131, 84823929121 | 3.9968387894666656e+23 |
| test_perimetr_int                  |         63, 56, 89         | 208                    |
| test_zero_perimetr                 |          0, 0, 0           | 0                      |
## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (a * h)\2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
-Triangle: P = a + b + c
