# **Geometric_lib**

## Descripiton
##### Calling the appropriate function with the required parameters.

## Description of the functions
### Circle
**Area function area(r)**
>Takes a number `r` - the radius of a circle
Return area of circle.

**Call example**
```
area_circle = area(3)
```
**Perimeter function perimeter(r)**
>Takes a number `r` - the radius of a circle
Return perimeter of circle.

**Call example**
```
perimeter_circle = perimeter(3)
```
### Rectangle
**Area function area(a, b)**
>Accepted parameters: `(int) a`, `(int) b`.
Return area of rectangle.

**Call example**
```
area_rectangle = area(2, 6)
```
**Perimeter function perimeter(r)**
>Accepted parameters: `(int) a`, `(int) b`.
Return perimeter of rectangle.

**Call example**
```
perimeter_rectangle = perimeter(6, 2)
```
### Square
**Area function area(a)**
>Takes a number `a` (the side of a square), returns the area of the square.
Return area of square.

**Call example**
```
area_square = area(5)
```
**Perimeter function perimeter(a)**
>Takes a number `a` (the side of a square), returns the perimeter of the square.
Return perimeter of square.

**Call example**
```
perimeter_square = perimeter(4)
```
### Triangle
**Area function area(a, h)**
>Accepted parameters: side `(int) a`, height `(int) h`.
Return area of triangle.

**Call example**
```
area_triangle = area(3, 7)
```
**Perimeter function perimeter(a, b, c)**
>Accepted parameters: side `(int) a`, side `(int) b`, side `(int) c`.
Return perimeter of triangle.

**Call example**
```
perimeter_triangle = perimeter(4, 6, 5)
```
## Project change history
>**Commit**: c0ee283
**Date**: Sep 12 2023
**Description**: error fix

>**Commit**: 21d25e9
**Date**: Sep 12 2023
**Description**: add new file

## Test cases

| №  | TestCase          | TestName        | given value | expected value    | received value    | status |
|----|-------------------|-----------------|-------------|-------------------|-------------------|--------|
| **1**  | **CircleTestCase**    | `test_zero_mul`   | 0           | 0                 | 0                 | **Passed** |
| **2**  | **CircleTestCase**    | `test_area`       | 5           | 78.53981633974483 | 78.53981633974483 | **Passed** |
| **3**  | **CircleTestCase**    | `test_perimeter`  | 5           | 31.41592653589793 | 31.41592653589793 | **Passed** |
| **4**  | **RectangleTestCase** | `test_zero_mul`   | 0, 2        | 0                 | 0                 | **Passed** |
| **5**  | **RectangleTestCase** | `test_square_mul` | 10, 10      | 100               | 100               | **Passed** |
| **6**  | **RectangleTestCase** | `test_area`       | 6, 2        | 12                | 12                | **Passed** |
| **7**  | **RectangleTestCase** | `test_perimeter`  | 12, 56      | 136               | 136               | **Passed** |
| **8**  | **SquareTestCase**    | `test_zero_mul`   | 0           | 0                 | 0                 | **Passed** |
| **9**  | **SquareTestCase**    | `test_area`       | 8           | 64                | 64                | **Passed** |
| **10** | **SquareTestCase**    | `test_perimeter`  | 4           | 16                | 16                | **Passed** |
| **11** | **TriangleTestCase**  | `test_zero_mul`   | 0, 3        | 0                 | 0                 | **Passed** |
| **12** | **TriangleTestCase**  | `test_area`       | 4, 9        | 18                | 18                | **Passed** |
| **13** | **TriangleTestCase**  | `test_perimeter`  | 34, 7, 3    | 44                | 44                | **Passed** |

# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a