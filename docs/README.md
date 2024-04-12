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
    perimeter(2, 4)  # input : side, ground; output : 12  
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
    - The function accepts one number (int):
      - side : one side of the square;
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
    - The function accepts three numbers (float):
      - a : first side of the triangle;
      - b : second side of the triangle;
      - c : third side of triangle;
    - Returns the area of ​​a figure, namely the addition of all three sides (float).
  ```py
  if __name__ == "__main__":
    area(1.0, 3.0)             # height, ground : side; output : 1.5 
    perimeter(2.0, 3.0, 4.0)   # input : a, b and c, where they are sides of a triangle; output : 9.0  
  ```
# Project change history with commit hashes.

```
* commit 1b0783f7ca5683601ef57d4601dc4a75cf6a8d6f (HEAD -> upgrade-tests, main)
| Author: Erusalimcev Petr Vasilevich <114782849+klorainy@users.noreply.github.com>
| Date:   Fri Nov 17 06:21:05 2023 +0300
|
|     Improving tests by adding types of data to tests
* commit 615754d9ce49c72f1530416ee1718ac5fbbe0be0 (HEAD -> main, 4-labs)
| Author: Erusalimcev Petr Vasilevich <114782849+klorainy@users.noreply.github.com>
| Date:   Fri Nov 17 03:42:05 2023 +0300
|
|     Update readme.md
|
* commit 158ee61e60222efc535cfbb53b0e87471d53b7ab
| Author: Erusalimcev Petr Vasilevich <114782849+klorainy@users.noreply.github.com>
| Date:   Fri Nov 17 03:17:40 2023 +0300
|
|     Added unit tests
|
* commit 8131cd87902c1a29ccbfff526900d31406b03f10
| Author: Erusalimcev Petr Vasilevich <114782849+klorainy@users.noreply.github.com>
| Date:   Fri Nov 17 03:17:05 2023 +0300
|
|     Added data type check for functions
|
* commit 14ac63af35a3e63ca7984720b65d806113b1fb5d
| Author: Erusalimcev Petr Vasilevich <114782849+klorainy@users.noreply.github.com>
| Date:   Fri Oct 6 02:58:51 2023 +0300
|
|     Добавлены описания функций и примеры вызовов
|
* commit a01b69643efe095d406407fd889c4a1cd85b58d7
| Author: Erusalimcev Petr Vasilevich <114782849+klorainy@users.noreply.github.com>
| Date:   Fri Oct 6 02:42:37 2023 +0300
|
|     Добавлены описания функций и примеры их вызовов
|
* commit 488c90900869677af523c33fbb548aeb076166c6
| Author: Erusalimcev Petr Vasilevich <114782849+klorainy@users.noreply.github.com>
| Date:   Fri Oct 6 02:28:42 2023 +0300
|
|     Добавлены примеры вызовов функций
|
* commit 07027ab97d854b2af11ed263adc850c3b89adb6c
| Author: Erusalimcev Petr Vasilevich <114782849+klorainy@users.noreply.github.com>
| Date:   Fri Oct 6 02:23:01 2023 +0300
|
|     Добавлено общее описание функций
|
* commit 22800e731623f3f13297f82e881bb60749166116 (new_features_408596)
| Author: Erusalimcev Petr Vasilevich <114782849+klorainy@users.noreply.github.com>
| Date:   Fri Sep 8 22:00:23 2023 +0300
|
|     Ошибка в периметре исправлена.
|
* commit f30cf7e1b6b9130042824ba3771e47fa47136f9e
| Author: Erusalimcev Petr Vasilevich <114782849+klorainy@users.noreply.github.com>
| Date:   Fri Sep 8 21:50:35 2023 +0300
|
|     Добавлена последняя фигура 1 лабораторной.
|
* commit aa86678a435730f20855a7b1ccddd4b01e68e11e
| Author: Erusalimcev Petr Vasilevich <114782849+klorainy@users.noreply.github.com>
| Date:   Fri Sep 8 21:49:23 2023 +0300
|
|     Добавлена еще одна фигура.
|
* commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD)
| Author: smartiqa <info@smartiqa.ru>
| Date:   Thu Mar 4 14:55:29 2021 +0300
|
|     L-03: Docs added
|
* commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
  Author: smartiqa <info@smartiqa.ru>
  Date:   Thu Mar 4 14:54:08 2021 +0300

      L-03: Circle and square added

```
# Link to the original creator of my work.
- [dageron20](https://github.com/dageron20)
  
# Links to files
[^1]: [Circle](https://github.com/klorainy/fork_geometric_lib/blob/main/circle.py)
[^2]: [Rectangle](https://github.com/klorainy/fork_geometric_lib/blob/main/rectangle.py)
[^3]: [Square](https://github.com/klorainy/fork_geometric_lib/blob/main/square.py)
[^4]: [Triangle](https://github.com/klorainy/fork_geometric_lib/blob/main/triangle.py)
