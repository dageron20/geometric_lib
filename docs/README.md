# General description of the solution
The solution is designed to calculate the area and perimeter of shapes:
+ circle.py - for circle
+ rectangle.py - for rectangle
+ square.py - for square
+ triangle.py - for triangle



## Testing
Testing is based on the `unittest` module. A file was created for this `tests.py ` in the root directory of the project. In this file, the `BaseFigureTest` class is declared, which declares methods for testing the calculation of area, perimeter and checking exceptions that may occur during their calculation.

UnitTests `RectangleTest`, `SquareTest`, `TriangleTest` and `CircleTest` are inherited from `BaseFigureTest` and `unittest.TestCase`. In each of them, special tuples are declared, in which input and expected data are specified.


# UNIT_TESTS:
## Goals and objectives of testing:
The purpose of the testing was to verify the correct operation of the functions
to calculate the area and perimeter of shapes. The main objective of testing was
ensure that the area() and perimeter() functions return the expected values for
given parameters of the figures.
## Description of the tested product:
The product under test is a Python module that includes
area() and perimeter() functions, designed to calculate the area and perimeter of a circle
respectively.
## Testing area:
The test area is the specific functions area() and perimeter(), which
must correctly calculate the area and perimeter of shapes based on the given
values.
## Testing strategy:
For testing, a unit testing strategy was used. Were
test cases have been developed to verify the correctness of area calculations and
perimeter of figures at different values.
## Acceptance criteria:
The criteria for successful completion of testing were the completion of all test
cases without errors, as well as the coincidence of the calculated values of area and perimeter
with expected values.
## Expected results:
The expected test result is successful completion of all
test cases, absence of errors and coincidence of calculated values with
expected results.
Test results:
The test cases for the area() and perimeter() functions were executed successfully, and
The calculated values of area and perimeter coincided with the expected results.
Thus, the module for calculating the area and perimeter of a circle has been tested
successfully.




# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
