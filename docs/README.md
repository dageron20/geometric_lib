# General description of the solution
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

## Testing
Testing is based on the `unittest` module. A file was created for this `tests.py ` in the root directory of the project. In this file, the `BaseFigureTest` class is declared, which declares methods for testing the calculation of area, perimeter and checking exceptions that may occur during their calculation.

UnitTests `RectangleTest`, `SquareTest`, `TriangleTest` and `CircleTest` are inherited from `BaseFigureTest` and `unittest.TestCase`. In each of them, special tuples are declared, in which input and expected data are specified.

### class BaseFigureTest
1. There must be `self.module` attribute in your class.
2. There must be area and `perimeter` methods in your `self.module` class/module.
3. Your TestCase class must be inherited from `unittest.TestCase` class.

To test your methods:
+ There should be `self.area_testcases` dict with test cases to test `area` method.
    Testcase format: `((*args), answer)`
+ There should be `self.perimeter_testcases` dict with test cases to test `perimeter` method.
    Testcase format: `((*args), answer)`
+ There should be `self.exception_testcases` dict with test cases to test expected exceptions.
    Testcase format: `((*args), method, expected_exception)`

```python
import unittest
from test import BaseFigureTest

class SquareTest(BaseFigureTest, unittest.TestCase):
    def setUp(self):
        self.module = myPackage.SquareClass
        self.area_testcases = (
            ((2, ), 4), # testcase 1
            ((70, ), 4900), # testcase 2
        )
        self.perimeter_testcases = (
            ((2, ), 8), # testcase 1
            ((100, ), 400), # testcase 2
        )
        self.exception_testcases = (
            (('a', ), self.module.area, TypeError), # testcase 1
        )

if __name__ == '__main__:
    unittest.main()
```

### Usage
```bash
python -m unittest tests.py -v
```
### TestCases
<table>
  <thead>
    <tr>
      <th>Tested function</th>
      <th>Input</th>
      <th>Expected</th>
      <th>Test Result</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>circle.area</td>
      <td>(0,)</td>
      <td>0</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>circle.area</td>
      <td>(1,)</td>
      <td>3.141592653589793</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>circle.area</td>
      <td>(2,)</td>
      <td>12.566370614359172</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>circle.area</td>
      <td>(3,)</td>
      <td>28.274333882308138</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>circle.area</td>
      <td>(10,)</td>
      <td>314.1592653589793</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>circle.area</td>
      <td>(100,)</td>
      <td>31415.926535897932</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>circle.area</td>
      <td>(0.5,)</td>
      <td>0.7853981633974483</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>circle.area</td>
      <td>(1.3,)</td>
      <td>5.3092915845667505</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>circle.area</td>
      <td>('a',)</td>
      <td>TypeError</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>circle.perimeter</td>
      <td>('a',)</td>
      <td>TypeError</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>circle.perimeter</td>
      <td>(0,)</td>
      <td>0</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>circle.perimeter</td>
      <td>(1,)</td>
      <td>6.283185307179586</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>circle.perimeter</td>
      <td>(2,)</td>
      <td>12.566370614359172</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>circle.perimeter</td>
      <td>(3,)</td>
      <td>18.84955592153876</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>circle.perimeter</td>
      <td>(10,)</td>
      <td>62.83185307179586</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>circle.perimeter</td>
      <td>(100,)</td>
      <td>628.3185307179587</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>circle.perimeter</td>
      <td>(0.5,)</td>
      <td>3.141592653589793</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>circle.perimeter</td>
      <td>(1.3,)</td>
      <td>8.168140899333462</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>(10, 0)</td>
      <td>0</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>(0, 0)</td>
      <td>0</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>(0, 10)</td>
      <td>0</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>(10, 10)</td>
      <td>100</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>(5, 5)</td>
      <td>25</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>(100, 100)</td>
      <td>10000</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>(5, 3)</td>
      <td>15</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>(3, 5)</td>
      <td>15</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>(100, 1)</td>
      <td>100</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>(1, 100)</td>
      <td>100</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>(0.2, 0.2)</td>
      <td>0.4</td>
      <td>FAILED</td>
      <td>Language Feature: 0.04 becomes 0.04000000000000001</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>('a', 'a')</td>
      <td>TypeError</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.area</td>
      <td>({}, 1)</td>
      <td>TypeError</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>('a', 4)</td>
      <td>TypeError</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>(0, 0)</td>
      <td>0</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>(5, 4)</td>
      <td>18</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>(10, 0)</td>
      <td>20</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>(0, 10)</td>
      <td>20</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>(10, 10)</td>
      <td>40</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>(20, 20)</td>
      <td>80</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>(13, 13)</td>
      <td>52</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>(10, 20)</td>
      <td>60</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>(20, 10)</td>
      <td>60</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>(13, 12)</td>
      <td>50</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>(1, 2)</td>
      <td>6</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>rectangle.perimeter</td>
      <td>(0.1, 0.2)</td>
      <td>0.6</td>
      <td>FAILED</td>
      <td>Language Feature: 0.6 becomes 0.6000000000000001</td>
    </tr>
    <tr>
      <td>square.area</td>
      <td>(10,)</td>
      <td>100</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>square.area</td>
      <td>(0,)</td>
      <td>0</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>square.area</td>
      <td>(1,)</td>
      <td>1</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>square.area</td>
      <td>(2,)</td>
      <td>4</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>square.area</td>
      <td>(70,)</td>
      <td>4900</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>square.area</td>
      <td>('a',)</td>
      <td>TypeError</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>square.perimeter</td>
      <td>(0,)</td>
      <td>0</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>square.perimeter</td>
      <td>(1,)</td>
      <td>4</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>square.perimeter</td>
      <td>(2,)</td>
      <td>8</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>square.perimeter</td>
      <td>(100,)</td>
      <td>400</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>square.perimeter</td>
      <td>(15,)</td>
      <td>60</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>square.perimeter</td>
      <td>(3,)</td>
      <td>12</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>square.perimeter</td>
      <td>(0.1,)</td>
      <td>0.4</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>square.perimeter</td>
      <td>(0.01,)</td>
      <td>0.04</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>square.perimeter</td>
      <td>('a',)</td>
      <td>aaaa</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>(0, 1)</td>
      <td>0</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>(1, 0)</td>
      <td>0</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>(0, 100)</td>
      <td>0</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>(100, 0)</td>
      <td>0</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>(5, 3)</td>
      <td>7.5</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>(3, 3)</td>
      <td>4.5</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>(10, 10)</td>
      <td>50</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>(30, 70)</td>
      <td>1050</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>(0.5, 0.5)</td>
      <td>0.125</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>('a', 'b')</td>
      <td>TypeError</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>('a', 1)</td>
      <td>TypeError</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.area</td>
      <td>(1, 'a')</td>
      <td>TypeError</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.perimeter/td>
      <td>(1, 'a', 'a')</td>
      <td>TypeError</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>('a', 1, 'a')</td>
      <td>TypeError</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>('a', 'a', 1)</td>
      <td>TypeError</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>(0, 0, 0)</td>
      <td>0</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>(0, 0, 1)</td>
      <td>1</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>(0, 1, 0)</td>
      <td>1</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>(1, 0, 0)</td>
      <td>1</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>(1, 2, 3)</td>
      <td>6</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>(3, 2, 1)</td>
      <td>6</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>(3, 3, 3)</td>
      <td>9</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>(100, 100, 100)</td>
      <td>300</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>(0.5, 0.5, 0.5)</td>
      <td>1.5</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>('a', 'b', 'c')</td>
      <td>abc</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>triangle.perimeter</td>
      <td>('c', 'b', 'a')</td>
      <td>cba</td>
      <td>OK</td>
    </tr>
  </tbody>
</table>

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
## UnitTests

Commit: b545953b235cb5cbfbd9ee472956132e70879be8

Date: 16.11.2023

Testing exceptions, classes `BaseAreaTestCase` and `BasePerimeterTestCase` merged to class `BaseFigureTest`

## UnitTests

Commit: 54153e0c0125a867a1d38657b390c3fcc4052f40

Date: 01.11.2023

UnitTests created for the `area()` and `perimeter()` functions in modules `circle.py`, `rectangle.py`, `square.py`, `triangle.py`

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
