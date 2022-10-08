"""
Итераторы и Генераторы - домашнее задание
"""
import random as rd
"""
Задача 1

Создайте генератор, который создает квадраты чисел, вплоть до некоторого числа N.
"""


def gensquares(n):
    for a in range(n):
        yield a ** 2


for x in gensquares(10):
    print(x)

"""
Задача 2

Создайте генератор, который возвращает "n" случайных чисел между нижней и 
верхней границами (границы являются параметрами функции).
Замечание: используйте библиотеку random. Например:
"""


def rand_num(low, high, n):
    for a in range(n):
        yield rd.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)


"""
Задача 3

Используйте функцию iter(), чтобы превратить строку ниже в итератор:
"""

s = 'hello'
b = iter(s)

print(next(b))


"""
Дополнительное задание!

Можете ли Вы объяснить, что такое gencomp в коде ниже? 
(Замечание: Мы не рассматривали это на лекциях. Вам может понадобится поиск в 
Google или Stack Overflow, чтобы найти ответ!)

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

4
5

Подсказка: Ищите в Google фразу generator comprehension!
"""