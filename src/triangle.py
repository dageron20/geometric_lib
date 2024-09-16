def area(a, h):
	''' 
	Возвращает площадь треугольника

		Параметры:
			a (int): основание треугольника
			h (int): высота треугольника

		Возвращаемое значение:
			a * h / 2: искомая площадь треугольника
	'''

	if (type(a) is not int or type(h) is not int):
		raise TypeError("Аргументы должен быть int")

	if (a <= 0 or h <= 0):
		raise ValueError("Аргументы должны быть больше ноля")

	return a * h / 2

def perimeter(a, b, c):
	''' 
	Возвращает периметр треугольника

		Параметры:
			a (int): одна сторона треугольника
			b (int): вторая сторона треугольника
			c (int): третья сторона треугольника

		Возвращаемое значение:
			a + b + c: искомый периметр треугольника
	'''

	if (type(a) is not int or type(b) is not int or type(c) is not int):
		raise TypeError("Аргументы должен быть int")

	if (a <= 0 or b <= 0 or c <= 0):
		raise ValueError("Аргументы должны быть больше ноля")

	return a + b + c