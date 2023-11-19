# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle S = a * h / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2sa + 2b
- Square: P = 4a
- Triangele P = a + b + c

# Documentation of functions
## circle.py
### area function
- Taken parametrs: r - circle radius
- Output: area of circle with current radius
- Execute: area(r)
- Example:
- area(10) Output: 314.1592653589793

### perimetr function
- Taken parametrs: r - circle radius
- Output: perimete of circle with current radius
- Execute: perimetr(r)
- Example:
- perimetr(10) Output: 62.83185307179586

## rectangle.py
### area function
- Taken parametrs: a, b - sides of rectangle
- Output: area of rectangle with current sides
- Execute: area(a, b)
- Example:
- area(10, 5) Output: 50
### perimetr function
- Taken parametrs: a, b - sides of rectangle
- Output: perimeter of rectangle with current sides
- Execute: perimetr(a, b)
- Example:
- perimetr(10, 5) Output: 30

## square.py
### area function
- Taken parametrs: a - side of square
- Output: area of square with current sides
- Execute: area(a)
- Example:
- area(10) Output: 100
### perimetr function
- Taken parametrs: a - side of square
- Output: perimeter of square with current sides
- Execute: perimetr(a)
- Example:
- perimetr(10) Output: 40

## triangle.py
### area function
- Taken parametrs: a - side of triangle, h - height passed to side a
- Output: area of triangle with current parametrs
- Execute: area(a, h)
- Example:
- area(10, 2) Output: 10
### perimetr function
- Taken parametrs: a, b, c - sides of triangle
- Output: perimeter of triangle with current parametrs
- Execute: perimetr(a, b, c)
- Example:
- perimetr(10, 8, 17) Output: 35

# Tests
| Название теста       | Входные данные        | Ожидаемый результат | Фактический результат |
|----------------------|-----------------------|---------------------|-----------------------|
| test_zero_value      | width=10, height=0    | area=0, perimeter=0 | 0, 0 |
| test_square_values   | width=10, height=10   | area=100            | 100 |
| test_different_values| width=2, height=5     | area=10, perimeter=14 | 10, 14 |
| test_float_values    | width=2.5, height=4.5| area=11.25 perimeter=14 | 11.25, 14 |
| test_negative_value  | width=-2, height=5 | Value Error            | -10, 6 |
| test_char_inputs     | width='a', height=2 | Type Error            | aa, Error |
| test_bool_inputs     | width=True, height=False | Type Error       | 0, 2 |
| test_zero_radius     | radius=0              | area=0, perimeter=0 | 0, 0 |
| test_natural_value   | radius=10             | area=314.1592653589793, perimeter=62.83185307179586| 314.1592653589793, 62.83185307179586 |
| test_negative_values | radius=-10            | Value Error         | 314.1592653589793 |
| test_float_values    | radius=2.2            |area=15.205308443374602 perimeter=20.734511513692635 | 15.205308443374602, 20.734511513692635 |
| test_char_inputs     | radius='a'            | Type Error          | Type Error |         
| test_bool_inputs     | radius=True           | Type Error          | 3.141592653589793 |       
| test_zero_value      | side_length=0         | area=0, perimeter=0 | 0, 0 |
| test_natural_value   | side_length=5         | area=25, perimeter=20 | 25, 20 |
| test_negative_values | side_length=-5        | Value Error         | 25 |
| test_float_values    | side_length=3.3       |area=4.840000000000001 perimeter=13.2 | 4.840000000000001, 13.2 |
| test_char_inputs     | side_length='a'       | Type Error          | Type Error, aaaa |         
| test_bool_inputs     | side_length=True      | Type Error          | 1, 4 | 
| test_zero_value      | base=5, height=0, side1=0, side2=0, side3=0 | area=0, perimeter=0  | 0, 0 |
| test_different_values| base=5, height=2, side1=5, side2=2, side3=3 | area=5.0, perimeter=10| 5.0, 10 |
| test_negative_values | base = -5, height=2, side1=-3 side2=2, side3=1 | Value Error | -5, 0 |
| test_float_values    | base=3.3, height=2.2, side1=1.1, side2=2.2, side3=3.3 | area = 3.63, perimeter = 6.6 | 3.63, 6.6 |
| test_char_inputs     | base='a', height='b', side1='a', side2='b', side3='c' | Type Error | Type Error, abc |
| test_char_inputs     | base=True, height=False, side1=True, side2=True, side3=False | Type Error | 0.0, 2 |

# History of commits
- added rectangle.py (commit id: 135c767)
- added triangle.py and fixed rectangle.py (commit id: eb8ebbb)
- added docummentation for rectangle.py (commit id: 6093618)
- added docummentation for triangle.py (commit id: 087c9a6)
- added docummentation for circle.py (commit id: 4162728)
- added docummentation for square.py (commit id: d5c1e5b)
- added tests.py(commit id: 161b4d0)