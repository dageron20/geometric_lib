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
| Test Name                 | Input        | Wanted Result        | Result            |
|---------------------------|--------------|----------------------|-------------------|
| test_area_zero            | r = 0        | 0                    | 0                 |
| test_area                 | r = 10       | π * 10^2 ≈ 314.16    | 314.16            |
| test_perimeter_zero       | r = 0        | 0                    | 0                 |
| test_perimeter            | r = 10       | 2 * π * 10 ≈ 62.83   | 62.83             |
| test_area_negative        | r = -5       | Error                | -78.54            |
| test_perimeter_negative   | r = -5       | Error                | -31.42            |
| test_area_non_numeric     | r = "string" | Error                | TypeError         |
| test_perimeter_non_numeric| r = "string" | Error                | TypeError         |
| test_area_boolean         | r = True     | Error                | 3.14              |
| test_perimeter_boolean    | r = True     | Error                | 6.28              |


## Square
| Test Name                 | Input        | Wanted Result | Result  |
|---------------------------|--------------|---------------|---------|
| test_area_zero            | a = 0        | 0             | 0       |
| test_area                 | a = 10       | 100           | 100     |
| test_perimeter_zero       | a = 0        | 0             | 0       |
| test_perimeter            | a = 10       | 40            | 40      |
| test_area_negative        | a = -5       | Error         | 25      |
| test_perimeter_negative   | a = -5       | Error         | -20     |
| test_area_non_numeric     | a = "string" | Error         | TypeError |
| test_perimeter_non_numeric| a = "string" | Error         | "stringstringstringstring" |
| test_area_boolean         | a = True     | Error         | 1       |
| test_perimeter_boolean    | a = True     | Error         | 4       |



## Rectangle
| Test Name                   | Input            | Wanted Result | Result      |
|-----------------------------|------------------|---------------|-------------|
| test_area_zero              | a = 10, b = 0    | 0             | 0           |
| test_area                   | a = 10, b = 10   | 100           | 100         |
| test_perimeter_zero         | a = 0, b = 0     | 0             | 0           |
| test_perimeter              | a = 10, b = 20   | 60            | 60          |
| test_area_negative          | a = -5, b = 20   | Error         | -100        |
| test_perimeter_negative     | a = -5, b = 20   | Error         | 30          |
| test_area_non_numeric       | a = "string", b = 20 | Error      | 'Repeated string output' |
| test_perimeter_non_numeric  | a = "string", b = 20 | Error      | TypeError   |
| test_area_boolean           | a = True, b = 20 | Error         | 20          |
| test_perimeter_boolean      | a = True, b = 20 | Error         | 42          |



## Triangle
| Test Name                   | Input                 | Wanted Result | Result      |
|-----------------------------|-----------------------|---------------|-------------|
| test_area_zero              | a = 10, h = 0         | 0             | 0           |
| test_area                   | a = 10, h = 5         | 25            | 25          |
| test_perimeter_zero         | a = 0, b = 0, c = 0   | 0             | 0           |
| test_perimeter              | a = 10, b = 15, c = 20| 45            | 45          |
| test_area_negative          | a = -5, h = 5         | Error         | -12.5       |
| test_perimeter_negative     | a = -5, b = 15, c = 20| Error         | 30          |
| test_area_non_numeric       | a = "string", h = 5   | Error         | TypeError   |
| test_perimeter_non_numeric  | a = "string", b = 15, c = 20 | Error   | TypeError   |
| test_area_boolean           | a = True, h = 5       | Error         | 2.5         |
| test_perimeter_boolean      | a = True, b = 15, c = 20 | Error       | 36          |
| test_existence              | a = 10, b = 50, c = 100 | Error       | 160          |
