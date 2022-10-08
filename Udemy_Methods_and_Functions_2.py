"""
Напишите функцию, которая вычисляет объём сферы по заданному радиусу.
Формула для объёма сферы:
"""


def vol(rad):
    """
    Функция вычисления объема сферы.
    """
    print(4/3*3.14*rad**3)


# Проверка
vol(2)


"""
Напишите функцию, которая проверяет, содержится ли число в указанном диапазоне
(включая верхнюю и нижнюю границы)

def ran_check(num,low,high + 1):
    pass

# проверка
ran_check(5,2,7)

5 is in the range between 2 and 7

Если Вы хотите вернуть только значение boolean:
"""


def ran_bool(num, low, high):
    """
    Функция проверяет диапазон на наличие в нем числа"""
    return num in range(low, high)


print(ran_bool(3, 4, 10))


"""
Напишите функцию Python, которая принимает на вход строку, и вычисляет
количество букв в верхнем регистре и в нижнем регистре.

Пример строки : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Ожидаемый результат :
Количество символов в верхнем регистре (No. of Upper case characters) : 4
Количество символов в нижнем регистре  (No. of Lower case Characters) : 33

Подсказка: Вам могут пригодиться следующие методы для строк: .isupper() and .islower()

При желании можете использовать модуль Collections для решения этой задачи!
"""


def up_low(s):
    """
    Подсчет кол-ва букв в верхнем и нижнем регистре.
    """
    h = 0
    l = 0
    for i in s:
        if i.isupper():
            h += 1
        elif i.islower():
            l += 1
    print("Количество цифр в верхнем регистре: " + str(h))
    print("Количество цифр в нижнем регистре: " + str(l))


st = 'Hello Mr. Rogers, how are you this fine Tuesday?'


up_low(st)


"""
Напишите функцию Python, которая получает на входе список, и возвращает
 новый список, содержащий уникальные элементы из первого списка.

Sample List : [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]
Unique List : [1, 2, 3, 4, 5]
"""


def unique_list(lst):
    print("Sample List : " + str(lst))
    a = set(lst)
    print("Unique List : " + str(list(a)))


unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])


"""
Напишите функцию Python, которая перемножает все числа в списке.

Пример списка : [1, 2, 3, -4]
Ожидаемый результат : -24
"""


def multiply(numbers):
    a = 1
    for i in numbers:
        a *= i
    print(a)


multiply([1, 2, 3, -4, -4])


"""
Напишите функцию Python, которая проверяет входную строку,
является ли эта строка палиндромом или нет.

Палиндром - это слово или фраза, которые одинаково читаются
слева направо и справа налево, например madam или nurses run.
"""


def palindrome(s):
    s = s.replace(' ', '')
    return s == s[::-1]


print(palindrome('helleh'))


"""
Напишите функцию Python, которая проверяет, является ли строка панграммой или нет.

Панграмма - это слово или фраза, которая содержат все буквы алфавита хотя бы один раз.
Например: "The quick brown fox jumps over the lazy dog"
"""
import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    a = list(alphabet)
    d_a = len(a)
    for i in range(0, len(str1)):
        for j in range(0, d_a):
            if str1.lower()[i] == a[j]:
                a.pop(j)
                d_a -= 1
                break
    return len(a) == 0


print(ispangram("The quick brown fox jumps over the lazy dog"))

