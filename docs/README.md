# Math formulas
## Area
###
Формула площади окружности:
- Circle: S = πR²
####
import math
####
def area(r):
  ####
  return math.pi * r * r
####
При r = 3
####
Output: 28.274333882308138
###
Формула площади прямоугольника:
- Rectangle: S = ab
####
def area(a, b):
  ####
  return a * b
####
При a = 4, b = 5
####
Output: 20
###
Формула площади квадрата:
- Square: S = a²
####
def area(a):
  ####
  return a * a
####
При а = 4
####
Output: 16
###
Формула площади треугольника:
- Triangle: S = ah / 2
####
def area(a, h):
  ####
  return a * h / 2
####
При a = 5, h = 10
####
Output: 25
## Perimeter
###
Формула периметра окружности:
- Circle: P = 2πR
####
def perimeter(r):
  ####
  return 2 * math.pi * r
####
При r = 3
####
Output: 18.84955592153876
###
Формула периметра треугольника:
- Triangle: P = a + b + c
####
def perimeter(a, b, c):
  ####
  return a + b + c
####
При a = 5, b = 5, c = 5
####
Output: 15
###
Формула периметра прямоугольника:
- Rectangle: P = 2a + 2b
####
def perimeter(a, b):
  ####
  return (a + b) * 2
####
При a = 4, b = 5
####
Output: 18
###
Формула периметра квадрата:
- Square: P = 4a
####
def perimeter(a):
  ####
  return 4 * a
####
При a = 5
####
Output = 20
#
