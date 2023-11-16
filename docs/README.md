# Лабораторная работа 3
## unittest для файла rectangle.py
### расчет площади 
|Тест        |Входные данные|Expected     |Actual       |
|:----------:|:-------------|:-----------:|:-----------:|
|area(10,0)  |a=10,b=0      |Invalid input|Invalid input|
|area(2,3)   |a=2,b=3       |6            |6            |
|area(3,"A") |a=3,b="A"     |Invalid input|Invalid input|
|area(3,-1)  |a=3,b=-1      |Invalid input|Invalid input|
|area(2.3,3) |a=2.3,b=3     |Invalid input|Invalid input|
|area(3,True)|a=3,b=True    |Invalid input|Invalid input|
### расчет периметра
|Тест        |Входные данные|Expected     |Actual       |
|:----------:|:-------------|:-----------:|:-----------:|
|area(10,0)  |a=10,b=0      |Invalid input|Invalid input|
|area(2,3)   |a=2,b=3       |10           |10           |
|area(3,"A") |a=3,b="A"     |Invalid input|Invalid input|
|area(3,-1)  |a=10,b=-1     |Invalid input|Invalid input|
|area(2.3,3) |a=10,b=2.3    |Invalid input|Invalid input|
|area(3,True)|a=3,b=True    |Invalid input|Invalid input|
## unittest для файла circle.py
### расчет площади
|Тест        |Входные данные|Expected     |Actual       |
|:----------:|:-------------|:-----------:|:-----------:|
|area(0)     |a=0           |Invalid input|Invalid input|
|area(2)     |a=2           |12.56        |12.56        |
|area("A")   |a="A"         |Invalid input|Invalid input|
|area(-4)    |a=-4          |Invalid input|Invalid input|
|area(12.888)|a=12.888      |Invalid input|Invalid input|
|area(True)  |a=True        |Invalid input|Invalid input|
### расчет периметра
|Тест        |Входные данные|Expected     |Actual       |
|:----------:|:-------------|:-----------:|:-----------:|
|area(0)     |a=0           |Invalid input|Invalid input|
|area(2)     |a=2           |12.56        |12.56        |
|area("A")   |a="A"         |Invalid input|Invalid input|
|area(-4)    |a=-4          |Invalid input|Invalid input|
|area(2.9)   |a=2.9         |Invalid input|Invalid input|
|area(True)  |a=True        |Invalid input|Invalid input|
## unittest для файла square.py
### расчет площади
|Тест        |Входные данные|Expected     |Actual       |
|:----------:|:-------------|:-----------:|:-----------:|
|area(0)     |a=0           |Invalid input|Invalid input|
|area(2)     |a=2           |12.56        |12.56        |
|area("A")   |a="A"         |Invalid input|Invalid input|
|area(-4)    |a=-4          |Invalid input|Invalid input|
|area(1.7)   |a=1.7         |Invalid input|Invalid input|
|area(True)  |a=True        |Invalid input|Invalid input|
### расчет периметра
|Тест        |Входные данные|Expected     |Actual       |
|:----------:|:-------------|:-----------:|:-----------:|
|area(0)     |a=0           |Invalid input|Invalid input|
|area(2)     |a=2           |8            |8            |
|area("A")   |a="A"         |Invalid input|Invalid input|
|area(-4)    |a=-4          |Invalid input|Invalid input|
|area(9.3)   |a=9.3         |Invalid input|Invalid input|
|area(True)  |a=True        |Invalid input|Invalid input|
## unittest для файла triange.py
### расчет площади
|Тест           |Входные данные|Expected     |Actual       |
|:-------------:|:-------------|:------------:|:-----------:|
|area(0,10)     |a=0,h=10       |Invalid input|Invalid input|
|area(2,3)      |a=2,h=3        |3            |3            |
|area("A",3)    |a="A",h=3      |Invalid input|Invalid input|
|area(2,-3)     |a=2,h=-3       |Invalid input|Invalid input|
|area(2.3,1)    |a=2.3,h=1      |Invalid input|Invalid input|
|area(True,1)   |a=True,1       |Invalid input|Invalid input|
### расчет периметра
|Тест            |Входные данные|Expected     |Actual       |
|:--------------:|:-------------|:-----------:|:-----------:|
|area(0,1,2)     |a=0,b=1,c=2   |Invalid input|Invalid input|
|area(3,4,5)     |a=3,b=4,c=5   |12           |12           |
|area("A",2,3)   |a="A",b=2,c=3 |Invalid input|Invalid input|
|area(-2,2,3)    |a=-2,b=2,c=3  |Invalid input|Invalid input|
|area(2.99,2,3)  |a=2.99,b=2,c=3|Invalid input|Invalid input|
|area(True,2,3)  |a=True,b=2,c=3|Invalid input|Invalid input|

