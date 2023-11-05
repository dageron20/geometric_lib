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
| test_zero_value      | width=10, height=0    | area=0, perimeter=0  | true |
| test_square_values   | width=10, height=10   | area=100             | true |
| test_different_values| width=2, height=5     | area=10, perimeter=14| true |
| test_zero_radius     | radius=0              | area=0, perimeter=0  | true |
| test_natural_value_test| radius=10            | area=314.1592653589793, perimeter=62.83185307179586| true |
| test_zero_value      | side_length=0         | area=0, perimeter=0  | true |
| test_natural_value   | side_length=5         | area=25, perimeter=20| true |
| test_zero_value      | base=5, height=0      | area=0, perimeter=0  | true |
| test_different_values| base=5, height=2      | area=5.0, perimeter=10| true |

# History of commits
- added rectangle.py (commit id: 135c767)
- added triangle.py and fixed rectangle.py (commit id: eb8ebbb)
- added docummentation for rectangle.py (commit id: 6093618)
- added docummentation for triangle.py (commit id: 087c9a6)
- added docummentation for circle.py (commit id: 4162728)
- added docummentation for square.py (commit id: d5c1e5b)
- added tests.py(commit id: 161b4d0)