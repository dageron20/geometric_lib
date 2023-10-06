# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ab / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# What is included in the project?
> Here are various functions for finding the areas and perimeters of shapes.
1. Circle[^1]
  - The functions take float values ​​and returns them accordingly.
  - area:
    - This function is designed to calculate the area of ​​a circle;
    - The function uses a single number (floating point):
      - radius: circle radius;
    - Returns the area of ​​a figure, namely radius to the second power multiplied by pi (float);
  - perimeter:
    - This function is designed to calculate the perimeter of ​​a circle
    - The function uses a single number (floating point):
      - radius: circle radius;
    - Returns the perimeter of the figure, namely radius multiplied by 2 and pi (float).
  ```py
  if __name__ == "__main__":
    area(1.0)       # input : radius; output : 3.141592653589793
    perimeter(1.0)  # input : radius; output : 6.283185307179586  
  ```
2. Rectangle[^2]
  - The functions accept integer values ​​and returns them accordingly.
  - area:
    - This function is designed to calculate the area of ​​a rectangle;
    - The function accepts two numbers (int):
      - side : value of the side of the rectangle;
      - ground : value of the base of the rectangle;
    - Returns the area of ​​the figure, namely multiplying side by ground (int);
  - perimeter:
    - This function is designed to calculate the perimeter of ​​a rectangle;
    - The function accepts two numbers (int):
      - side : value of the side of the rectangle;
      - ground : value of the base of the rectangle;
    - Returns the perimeter of a figure, namely the addition of the bases and sides (int).
  ```py
  if __name__ == "__main__":
    area(1, 3)       # input : side, ground; output : 3
    perimeter(2, 4)  # input : side, ground; output : : 12  
  ```
3. Square[^3]
  - The functions accept integer values ​​and returns them accordingly.
  - area:
    - This function is designed to calculate the area of ​​a square;
    - The function accepts one number (int):
        - side : one side of the square;
    - Returns the area of ​​the figure, namely side multiplied by side (int);
  - perimeter:
    - This function is designed to calculate the area of ​​a square;
    -  The function accepts one number (int):
      -  side : one side of the square;
    - Returns the perimeter of the figure, namely side multiplied by 4 (int).
  ```py
  if __name__ == "__main__":
    area(5)       # input : side; output : 25
    perimeter(5)  # input : side; output : 20
  ```
4. Triangle[^4]
  - The functions take float values ​​and returns them accordingly.
  - area:
    - This function is designed to calculate the area of ​​a triangle;
    - The function accepts two numbers (float):
      - height : the value of the height adjacent to one of the sides of the triangle;
      - ground : the value of the base of the triangle, otherwise the side to which the height is lowered;
    - Returns the area of ​​the figure, namely ground multiplied by height divided by hit (float).
  - perimeter:
    - This function is designed to calculate the area of ​​a triangle;
    - The function accepts two numbers (float):
    - The function accepts three numbers (float):
      - a : first side of the triangle;
      - b : second side of the triangle;
      - c : third side of triangle;
    - Returns the area of ​​a figure, namely the addition of all three sides (float).
  ```py
  if __name__ == "__main__":
    area(1.0, 3.0)             # input : side; output : 1.5 
    perimeter(2.0, 3.0, 4.0)   # input : a, b and c, where they are sides of a triangle; output : 9.0  
  ```
# Project change history with commit hashes.

```
* 14ac63a (HEAD -> main) Добавлены описания функций и примеры вызовов
* a01b696 Добавлены описания функций и примеры их вызовов
* 488c909 Добавлены примеры вызовов функций
* 07027ab Добавлено общее описание функций
* 22800e7 (new_features_408596) Ошибка в периметре исправлена.
* f30cf7e Добавлена последняя фигура 1 лабораторной.
* aa86678 Добавлена еще одна фигура.
* d078c8d (origin/main, origin/HEAD) L-03: Docs added
* 8ba9aeb L-03: Circle and square added
```
# Link to the original creator of my work.
- [dageron20](https://github.com/dageron20)
  
# Links to files
[^1]: [Circle](https://github.com/klorainy/fork_geometric_lib/blob/main/circle.py)
[^2]: [Rectangle](https://github.com/klorainy/fork_geometric_lib/blob/main/rectangle.py)
[^3]: [Square](https://github.com/klorainy/fork_geometric_lib/blob/main/square.py)
[^4]: [Triangle](https://github.com/klorainy/fork_geometric_lib/blob/main/triangle.py)
