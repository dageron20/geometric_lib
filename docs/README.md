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
