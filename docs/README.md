# Math formulas
## Area
- Circle: S = πR²  
	Данная формула нужна для нахождения **площади круга**.
  	Нужно импортировать библиотеку **math**, чтобы из неё взять число _пи_.
  
	На вход поступит значение радиуса данного круга.
	На выходе получится число, равное числу _пи_ умноженного на R<sup>2</sup>.

	```py
	def circle(r):
 		return r ** 2 * math.pi
 	```
 
- Rectangle: S = ab
	Данная формула нужна для вычислия **площади треугольника**. 
	На вход поступает 2 числа: 
			a: длина одной из сторон прямогульника
			b: длина другой стороны прямоугольника.
	На выходе получится число, равное произведению числе a и b.

	```py
 	def rectangle(a, b):
 		return a * b
 	```
 
- Square: S = a²
	Данная формула нужна для вычисления **площади квадрата**. 
	На вход поспупает число:
		a: длина стороны квадрата
	На выходе получится число a<sup>2</sup>.

	```py
 	def square(a):
 		return a ** 2
 	```

## Perimeter
- Circle: P = 2πR

	Данная формула нужна для вычисление **периметра круга**.
	Нужно импортировать библиотеку math для того, чтобы использовать число _пи_(3,1415926...).
	На вход поступает число R, равное радиусу окружности.
	На выходе получается число равное произведению 2 на радиус окружности и на число пи.

	```py
 	def circle(R):
 		return 2 * math.pi * R
 	```
 
- Rectangle: P = 2a + 2b

	Данная формула нужна для вычисления **периметра прямоугольника**.
	На вход поступает 2 числа:
		a: длина одной из сторон прямоугольника
		b: длина другой стороны прямоугольника
	На выходе должно получиться число, равное сумме удвоенных длин сторон прямоугольника.

	```py
 	def rectangle(a, b):
 		return 2 * a + 2 * b
 	```

- Square: P = 4a

	Данная формула нужна для вычисления **периметра квадрата**.
	На вход поступает число a, равное длине стороны квадрата.
	На выхоже получится число, равное произведению 4 на a.

	```py
 	def square(a):
 		return 4 * a
 	```
 # Unittests

|название теста| входные данные |    ожидание   | результат     |
|     :---:    |     :---:      |     :---:     |   :---:       |
|int, rectangle|a = 5, b = 4    |  20           | 20            |
|0, rectangle  |a = 0, b = 5    |"Invalid input"|"Invalid Input"|
|float, circle |a = 1.1         |3.7993         | 3.7993        |
|- int, circle |a = -1          |"Invalid input"|"Invalid input"|
|str, square   |a = "a"         |"Invalid input"|"Invalid input"|
|bool, square  |a = True        |"Invalid input"|"Invalid input"|
|int, triangle |a = 1, b = 2    | 1             | 1             |
|-int, triangle|a = -1,b = c = 2|"Invalid input"|"Invalid input"|

## types unittests

- Integer
 ```py
a = 5
b = 0
c = -1
```

- String
```py
a = "papa"
```

- Boolean
```py
a = True
b = False
```

- Float
```py
a = 1.1
```

- List
```py
a = [123, "papa", 12.3]
```

- Dictionaries
```py
a = {"mama": "papa"}
```

- Tuples
```py
a = (123, "papa", 12.3)
```

- Sets
```py
a = {"a", "b"}
```

- Enter
```py
a = '\n'
```

### Также были проведены такие тесты как:

- Nothing
```
на вход ничего не поступает
```

- Space
```
пользователь вводит пробел
```

- Overflow
```
пользователь вводит излишние данные
```

### Результаты тестов

Первый вызов **unittests** показал недочёты в коде.
Они были оперативно устранены.
При втором вызове **unittests** все тесты кроме **Overflow** были пройдены успешно.

# project modification history
```
  51dab6ad09b32019d3078197b1706b1853ce569f (HEAD -> main) corrected an annotation to the triatgle file
  a85333ec9ebf037b504b35aff9cf225f812e7b54 corrected an annotation to the square file
  2c69c83bc208850694f28485710dfaa6da32a8b2 corrected an annotation to the rectangle file
  3377fb2472d2e407ebdeab68badcf055f9d87d4d added an annotation to the README file with a detailed description of the functions and call examples
  28305f511aa1708efc19e3ab4370be2ee2389a73 added annotation to files rectangle, square, triangle
  de2fc05c098f111c3e90163026dceef5647ef371 added an annotation to the file circle
  8ec2e6903530be7cdd92a13b2756d41d215a39e6 added a def file with an annotation
  10191788228947bda6fcbab6e196ffce55e49344 (new_features_408606) corrected the mistace rectangle
  fddfc8e000ad3d78bbd867bd1f7978c75f9b4da1 add triangle
  9d47ebd1584d78745fb7dfd5fdd6783f3bbb7a73 add rectangle
  0c1ac2fbd755e29d501763cc1d93aae04d0098c1 (origin/main, origin/HEAD) corrected the mistake rectangle.py
  109ca664e7571b5a14eda224e2bcc8cd34b14a28 add triangle.py
  d95b85248f7b9dbab8ffdaf90d686aaf83960588 add rectangle.py
  d078c8d9ee6155f3cb0e577d28d337b791de28e2 L-03: Docs added
  8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added
```
