# Unittester.py

Файл включает в себя класс, содержащий тесты функций основных программ.

## rectangle.py
Тест проверяет на корректность работы функции area в файле rectangle.py

| FILE | Test name | function | Input | Expected | Status|
| --- | --- | --- | --- | --- | --- |
| rectangle.py | test_rectangle_area | area | ```10, 0``` | ```0``` | OK
| rectangle.py | test_rectangle_area | area | ```1123441, 5643234``` | ```6339840448194``` | OK
| rectangle.py | test_rectangle_area | area | ```"1123441", "5643234"``` | ```6339840448194``` | ERROR

Тест проверяет на корректность работы функции perimeter в файле rectangle.py

| FILE | Test name | function | Input | Expected | Status|
| --- | --- | --- | --- | --- | --- |
| rectangle.py | test_rectangle_perimeter | perimeter | ```15, 0``` | ```30``` | OK
| rectangle.py | test_rectangle_perimeter | perimeter | ```354, 321``` | ```1350``` | OK
| rectangle.py | test_rectangle_perimeter | perimeter | ```"354", "321"``` | ```1350``` | ERROR

## square.py
Тест проверяет на корректность работы функции area в файле square.py

| FILE | Test name | function | Input | Expected | Status|
| --- | --- | --- | --- | --- | --- |
| square.py | test_square_area | area | ```11324``` | ```128232976``` | OK
| square.py | test_square_area | area | ```-11``` | ```121``` | OK
| square.py | test_square_area | area | ```"-11"``` | ```121``` | ERROR

Тест проверяет на корректность работы функции perimeter в файле square.py

| FILE | Test name | function | Input | Expected | Status|
| --- | --- | --- | --- | --- | --- |
| square.py | test_square_perimeter | perimeter | ```153``` | ```612``` | OK
| square.py | test_square_perimeter | perimeter | ```312``` | ```1248``` | OK
| square.py | test_square_perimeter | perimeter | ```"312"``` | ```1248``` | ERROR

## circle.py
Тест проверяет на корректность работы функции area в файле circle.py

| FILE | Test name | function | Input | Expected | Status|
| --- | --- | --- | --- | --- | --- |
| circle.py | test_circle_area | area | ```14``` | ```615.7521601035994``` | OK
| circle.py | test_circle_area | area | ```164``` | ```84496.27601095107``` | OK
| circle.py | test_circle_area | area | ```"164"``` | ```84496.27601095107``` | ERROR

Тест проверяет на корректность работы функции perimeter в файле circle.py

| FILE | Test name | function | Input | Expected | Status|
| --- | --- | --- | --- | --- | --- |
| circle.py | test_circle_perimeter | perimeter | ```15``` | ```94.24777960769379``` | OK
| circle.py | test_circle_perimeter | perimeter | ```3``` | ```18.84955592153876``` | OK
| circle.py | test_circle_perimeter | perimeter | ```"3"``` | ```18.84955592153876``` | ERROR

## triangle
Тест проверяет на корректность работы функции area в файле triangle.py

| FILE | Test name | function | Input | Expected | Status|
| --- | --- | --- | --- | --- | --- |
| triangle.py | test_triangle_area | area | ```15, 48``` | ```360``` | OK
| triangle.py | test_triangle_area | area | ```15, 43``` | ```322.5``` | OK
| triangle.py | test_triangle_area | area | ```"15", "43"``` | ```322.5``` | ERROR

Тест проверяет на корректность работы функции perimeter в файле triangle.py

| FILE | Test name | function | Input | Expected | Status|
| --- | --- | --- | --- | --- | --- |
| triangle.py | test_triangle_perimeter | area | ```13, 323, 32``` | ```368``` | OK
| triangle.py | test_triangle_perimeter | area | ```13, 33, 32``` | ```78``` | OK
| triangle.py | test_triangle_perimeter | area | ```"13", "33", "32"``` | ```78``` | ERROR
| triangle.py | test_triangle_perimeter | area | ```100000, 1000000, 1``` | ```-1``` | ERROR
