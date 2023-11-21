# Function for calculation math formulas

## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a(h / 2)

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Functions
### Circle
- **area**: takes a number r, returns the area of a circle with radius r
```
Syntax: area(r) 
e.g. area(5) = 78.5398
```

- **perimeter**: takes a number r, returns the perimeter (length) of a circle with radius r
```
Syntax: perimteter(r) 
e.g. perimeter(2) = 12.5664
```

### Rectangle
- **area**: takes numbers a and b, returns the area of a rectangle with width a and length b
```
Syntax: area(a, b) 
e.g. area(10, 2) = 20
```

- **perimeter**: takes numbers a and b, returns the perimeter of a rectangle with width a and length b
```
Syntax: perimeter(a, b) 
e.g. perimeter(3, 4) = 14
```

### Square
- **area**: takes a number a, returns the area of a square with side length a
```
Syntax: area(a) 
e.g. area(5) = 25
```

- **perimeter**: takes a number a, returns the perimeter of a square with side length a
```
Syntax: perimeter(a) 
e.g. perimeter(40) = 160
```

### Triangle
- **area**: takes numbers a and h, returns the area of a triangle with side length a and height h
```
Syntax: area(a, h) 
e.g. area(5, 4) = 10
```

- **perimeter**: takes numbers a, b and c, returns the perimeter of a triangle with side lengths a, b and c
```
Syntax: perimeter(a, b, c) 
e.g. perimeter(1, 2, 3) = 6
```

## History of project changes

### cc9bb00
- Added new file rectangle.py

### 749353b
- Fixed error in file rectangle.py
- Added new file triangle.py

### new commit
- Added unit-tests


| № | Groups             | Name             | Input data        | Expected output data | Received output     | Status |
|---|--------------------|------------------|-------------------|----------------------|---------------------|--------|
| 1 | CircleTestCase     | test_zero_mul    | 0                 | 0                    | 0                   | Passed |
| 2 | CircleTestCase     | test_area        | 3                 | 28.274333882308138   | 28.274333882308138  | Passed |
| 3 | CircleTestCase     | test_area        | 100               | 31415.926535897932   | 31415.926535897932  | Passed |
| 4 | CircleTestCase     | test_area        | 25.6              | 2058.874161456607    | 2058.874161456607   | Passed |
| 5 | CircleTestCase     | test_area        | 0.51              | 0.8171282491987052   | 0.8171282491987052  | Passed |
| 6 | CircleTestCase     | test_area        | 9492349           | 283072230705944.7    | 283072230705944.7   | Passed |
| 7 | CircleTestCase     | test_perimeter   | 15                | 94.24777960769379    | 94.24777960769379   | Passed |
| 8 | CircleTestCase     | test_perimeter   | 191               | 1200.088393671301    | 1200.088393671301   | Passed |
| 9 | CircleTestCase     | test_perimeter   | 14.2              | 89.22123136195012    | 89.22123136195012   | Passed |
|10 | CircleTestCase     | test_perimeter   | 0.96              | 6.031857894892402    | 6.031857894892402   | Passed |
|11 | CircleTestCase     | test_perimeter   | 1941914           | 12201405.51260634    | 12201405.51260634   | Passed |
|12 | RectangleTestCase  | test_zero_mul    | 0, 5              | 0                    | 0                   | Passed |
|13 | RectangleTestCase  | test_zero_mul    | 6, 0              | 0                    | 0                   | Passed |
|14 | RectangleTestCase  | test_square_mul  | 5, 5              | 25                   | 25                  | Passed |
|15 | RectangleTestCase  | test_perimeter   | 4, 12             | 32                   | 32                  | Passed |
|16 | RectangleTestCase  | test_area        | 3, 5              | 15                   | 15                  | Passed |
|17 | RectangleTestCase  | test_area        | 100, 1            | 100                  | 100                 | Passed |
|18 | RectangleTestCase  | test_area        | 491941, 9349394   | 4599350233754        | 4599350233754       | Passed |
|19 | RectangleTestCase  | test_area        | 0.77, 0.26        | 0.20020000000000002  | 0.20020000000000002 | Passed |
|20 | RectangleTestCase  | test_area        | 1414.22, 199.942  | 282761.97524         | 282761.97524        | Passed |
|21 | RectangleTestCase  | test_perimeter   | 12, 22            | 68                   | 68                  | Passed |
|22 | RectangleTestCase  | test_perimeter   | 920, 195          | 2230                 | 2230                | Passed |
|23 | RectangleTestCase  | test_perimeter   | 38.3, 19.1        | 114.8                | 114.8               | Passed |
|24 | RectangleTestCase  | test_perimeter   | 0.524, 0.444      | 1.936                | 1.936               | Passed |
|25 | RectangleTestCase  | test_perimeter   | 84184841, 6461611 | 181292904            | 181292904           | Passed |
|26 | SquareTestCase     | test_zero_mul    | 0                 | 0                    | 0                   | Passed |
|27 | SquareTestCase     | test_zero_mul    | 0                 | 0                    | 0                   | Passed |
|28 | SquareTestCase     | test_area        | 4                 | 16                   | 16                  | Passed |
|29 | SquareTestCase     | test_area        | 50                | 2500                 | 2500                | Passed |
|30 | SquareTestCase     | test_area        | 42.1              | 1772.41              | 1772.41             | Passed |
|31 | SquareTestCase     | test_area        | 0.22              | 0.0484               | 0.0484              | Passed |
|32 | SquareTestCase     | test_area        | 22222222          | 493827150617284      | 493827150617284     | Passed |
|33 | SquareTestCase     | test_perimeter   | 7                 | 28                   | 28                  | Passed |
|34 | SquareTestCase     | test_perimeter   | 101               | 404                  | 404                 | Passed |
|35 | SquareTestCase     | test_perimeter   | 57.7              | 230.8                | 230.8               | Passed |
|36 | SquareTestCase     | test_perimeter   | 0.13              | 0.52                 | 0.52                | Passed |
|37 | SquareTestCase     | test_perimeter   | 99999999          | 399999996            | 399999996           | Passed |
|38 | TriangleTestCase   | test_zero_mul    | 0, 55             | 0                    | 0                   | Passed |
|39 | TriangleTestCase   | test_zero_mul    | 44, 0             | 0                    | 0                   | Passed |
|40 | TriangleTestCase   | test_area        | 4, 2              | 4                    | 4                   | Passed |
|41 | TriangleTestCase   | test_area        | 102, 1            | 51                   | 51                  | Passed |
|42 | TriangleTestCase   | test_area        | 4414121, 232323   | 512750916541.5       | 512750916541.5      | Passed |
|43 | TriangleTestCase   | test_area        | 0.55, 0.66        | 0.18150000000000002  | 0.18150000000000002 | Passed |
|44 | TriangleTestCase   | test_area        | 4154.22, 881.323  | 1830604.81653        | 1830604.81653       | Passed |
|45 | TriangleTestCase   | test_perimeter   | 10, 20, 30        | 60                   | 60                  | Passed |
|46 | TriangleTestCase   | test_perimeter   | 414, 252, 676     | 1342                 | 1342                | Passed |
|47 | TriangleTestCase   | test_perimeter   | 31.2, 52.2, 34.5  | 117.9                | 117.9               | Passed |
|48 | TriangleTestCase   | test_perimeter   | 0.111, 0.444,  0.777 | 1.332              | 1.332               | Passed |
|49 | TriangleTestCase   | test_perimeter   | 481284128, 21323131 | 512707270           | 512707270            | Passed |

