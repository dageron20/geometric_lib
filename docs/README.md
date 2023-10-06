# Solution:

# Description of function:
## Circle:
    import math

    - Импортирую библиотеку math для того чтобы использовать число пи

    def area(r):
    - Принимает число r, возвращает квадрат числа r, умноженный на число пи
        return math.pi * r * r

    def perimeter(r):
    - Принимает число r, возвращает число r умноженное на два и на число пи
        return 2 * math.pi * r
```
a = 2
print(area(a))
print(perimeter(a))
```       
## Rectangle:
    def area(a, b):
    - Принимает число a и число b, возвращает число a умноженное на число b
        return a * b

    def perimeter(a, b):
    - Принимает число a и число b, возвращает сумму чисел a и b, умноженную на 2
        return 2*(a + b)
## Square:
    def area(a):
    - Принимает число a, возвращает квадрат числа а
        return a * a

    def perimeter(a):
    - Принимает число a, возвращает число a умноженное на 4
        return 4 * a
## Tringle:
    def area(a, h):
    - Принимает число a и число h, возвращает среднее геометрическое чисел а и b
        return a * h / 2

    def perimeter(a, b, c):
    - Принимает число a, число b и число с, возвращает сумму чисел a,b,c
        return a + b + с

#History of project:
commit 0af89386f54bbb8cc6c67752bdc371216fc2958c (HEAD -> main, origin/main, origin/HEAD)
Author: viktoriagalakhova <viktoria.galakhova@gmail.com>
Date:   Thu Sep 21 19:55:37 2023 +0300

    fixed bug

commit cd51f4cb013930b09dcf7ab023be7b56b919f4ea
Author: viktoriagalakhova <viktoria.galakhova@gmail.com>
Date:   Thu Sep 21 19:52:17 2023 +0300

    add new file

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added

