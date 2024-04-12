# Unit tests
> The "tests" folder contains the files
> tests of the perimeter and area functions of various figures, which are presented in the "readme".
> Each shape test file includes a test case and a class with two functions: one for testing area, the other for perimeter.

## About functions
> All functions are focused on checking two key factors:
> * Checks whether the correct data type came into the function;
> * Check the correctness of calculations.
## All list of functions:
1) test_circle_area(self);
2) test_circle_perimeter(self);
3) test_rectangle_area(self);
4) test_rectangle_perimeter(self);
5) test_square_area(self);
6) test_square_perimeter(self);
7) test_triangle_area(self);
8) test_triangle_perimeter(self);
# Тест-кейсы unittest для файла circle.py
| Номер теста      | Входные данные |    Ожидаемый результат     |   Фактический результат    | Статус  |
|------------------|:--------------:|:--------------------------:|:--------------------------:|---------|        
| 1) area(r)       |     r = 5.0    |     78.53981633974483      |     78.53981633974483      | Успешно | 
| 2) area(r)       |     r = "123"  |         TypeError          |         TypeError          | Успешно |
# Тест-кейсы unittest для файла rectangle.py
| Номер теста         |     Входные данные      |    Ожидаемый результат     |   Фактический результат    | Статус  |
|---------------------|:-----------------------:|:--------------------------:|:--------------------------:|---------|        
| 1) area(s, g)       | s = (1, 2, 3), g = 93   |         TypeError          |         TypeError          | Успешно | 
| 2) perimeter(s, g)  | s = 111, g = "123"      |         TypeError          |         TypeError          | Успешно |
# Тест-кейсы unittest для файла square.py
| Номер теста      | Входные данные |    Ожидаемый результат     |   Фактический результат    | Статус  |
|------------------|:--------------:|:--------------------------:|:--------------------------:|---------|        
| 1) area(s)       |     s = 58     |           3364             |           3364             | Успешно | 
| 2) perimeter(s)  |     s = [1, 2] |         TypeError          |         TypeError          | Успешно |
# Тест-кейсы unittest для файла triangle.py
| Номер теста      |                     Входные данные                 |    Ожидаемый результат     |   Фактический результат    | Статус  |
|------------------|:--------------------------------------------------:|:--------------------------:|:--------------------------:|---------|        
| 1) area(g, h)    |  g = 11.172089799345672, h = 122.65544412571464    |    685.1588180755548       |     685.1588180755548      | Успешно | 
| 2) area(g, h)    |  g = 79.29024621114613, h = 23.84538410909948      |    945.3531885049246       |     945.3531885049246      | Успешно |
