# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Unit Tests
## Circle
| Test Name       | Input | Wanted Result | Result |
|----------------------|----------------|---------------------|----------------------|
| test_area_zero   | a = 0         | 0                 | 0                      |
| test_area       | a = 10          | 31,4....                   | 31,4....                     |
| test_perimeter_zero | a = 0       | 0                  | 0                     |
| test_perimeter    | a = 10         | 62,8...                   | 62,8...                     |

## Square
| Test Name          | Input  | Wanted Result | Result  |
|--------------------|--------|---------------|---------|
| test_area          | a = 10 | 100           | 100     |
| test_area_zero     | a = 0  | 0             | 0       |
| test_perimeter     | a = 10 | 40            | 40      |
| test_perimeter_zero| a = 0  | 0             | 0       |


## Rectangle
| Test Name          | Input     | Wanted Result | Result  |
|--------------------|-----------|---------------|---------|
| test_area          | a = 10, b = 10 | 100        | 100      |
| test_area_zero     | a = 10, b = 0 | 0         | 0       |
| test_perimeter     | a = 10, b = 20 | 60        | 60      |
| test_perimeter_zero| a = 0, b = 0  | 10        | 10      |



## Triangle
| Test Name          | Input           | Wanted Result | Result  |
|--------------------|-----------------|---------------|---------|
| test_area          | a = 10, h = 5   | 25            | 25      |
| test_area_zero     | a = 10, h = 0   | 0             | 0       |
| test_perimeter     | a = 10, b = 15, c = 20 | 45        | 45      |
| test_perimeter_zero| a = 0, b = 0, c = 0 | 0         | 0       |
| test_exist     | a = 1, b = 5, c = 10 | 0        | 16      |
