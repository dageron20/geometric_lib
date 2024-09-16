import math

def area(r):
	'''
	### Calculating the area of the circle

	:param r: `int`/`float` - radius of the circle
	:return: `int`/`float` - area of the circle

	```
	>>> area(5)
	>>> 78.53981633974483
	```
	'''
	return math.pi * r * r


def perimeter(r):
	'''
	### Calculating the perimeter of the circle

	:param r: `int`/`float` - radius of the circle
	:return: `int`/`float` - perimeter of the circle

	```
	>>> perimeter(5)
	>>> 31.41592653589793
	```
	'''
	return 2 * math.pi * r
