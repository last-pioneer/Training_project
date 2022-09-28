"""
Задачи Онлайн школы Udemy
Раздел Методы и Функции
"""

"""
Используйте for, .split() и if, чтобы написать команду,
 которая выведет слова, начинающиеся с буквы 's':
"""

st = 'Print only the words that start with s in this sentence'
mylist = st.split()
for i in mylist:
    if i[0] == 's':
        print(i)

"""
Используйте range(), чтобы распечатать все чётные числа от 0 до 10.
"""
mylist = []
for i in range(11):
    if i % 2 == 0:
        print(i)

"""
Используйте генератор списков, чтобы создать список всех чисел от 1 до 50, 
которые делятся нацело на 3.
"""

mylist = [x for x in range(0, 51) if x % 3 == 0]
print(mylist)

"""
Пройдите по словам в строке ниже, и если длина слова чётная, то напечатайте "Это слово имеет чётную длину!
"""
st = 'Print every word in this sentence that has an even number of letters'
mylist = st.split()
for i in mylist:
    if len(i) % 2 == 0:
        print(i, ' - Это слово имеет четную длину!')

"""
Напишите программу, которая напечатает числа от 1 до 100. Но для тех чисел, которые делятся нацело на 3, 
вместо числа выведите "Fizz", а для чисел которые делятся нацело на 5, выведите "Buzz". А для чисел, 
которые делятся нацело и на 3, и на 5, выведите "FizzBuzz".
"""

for i in range(0, 101):
    if i % 3 == 0 and i % 5 == 0 and i != 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

"""
Используйте генераторы списков, чтобы создать список первых букв из всех слов в строке ниже:
"""

st = 'Create a list of the first letters of every word in this string'
mylist = st.split()
mylist1 = [x[0] for x in mylist]
print(mylist1)

"""
Меньшее из двух чётных чисел: Напишите функцию, которая возвращает меньшее из двух чисел, 
если оба эти числа чётные. Иначе возвращает большее из двух чисел, если одно или оба числа нечётные.

lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
"""


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            print(a)
        else:
            print(b)
    else:
        if a > b:
            print(a)
        else:
            print(b)


lesser_of_two_evens(3, 5)


"""
animal_crackers: Напишите функцию, которая получает на входе строку из двух слов, 
и возвращает True если оба слова начинаются с одной и той же буквы.

animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
"""


def animal_crackers(text):
    a = text.split()
    b = a[0][0].split()
    c = a[1][0].split()
    if b == c:
        return True
    else:
        return False


print(animal_crackers('Crazy Kangaroo'))


"""
makes_twenty: На входе два числа, функция возвращает True если сумма этих чисел равна 20, 
или если одно из чисел равно 20. В противном случае, возвращает False.

makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
"""


def makes_twenty(n1, n2):
    if n1 + n2 == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False


print(makes_twenty(5, 1))


"""
OLD MACDONALD: Напишите функцию, которая переводит в верхний регистр первую и четвёртую буквы имени.

old_macdonald('macdonald') --> MacDonald

Замечание: 'macdonald'.capitalize() возвращает 'Macdonald'
"""


def old_macdonald(name):
    a = ""
    for let in range(len(name)):
        if let == 0 or let == 3:
            a += name[let].upper()
        else:
            a += name[let]
    return a


print(old_macdonald('macdonald'))


"""
master_yoda: На входе фраза, на выходе вернуть слова в обратном порядке.

master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'

Замечание: здесь может пригодиться метод .join(). Этот метод позволяет соединять строки, 
используя определенный разделитель. Вот пример для метода .join():

>>> "--".join(['a','b','c'])
>>> 'a--b--c'

Это значит, что если у Вас есть список слов и Вы хотите составить из них фразу, 
то можно соединить их, используя в качестве разделителя пробел:

>>> " ".join(['Hello','world'])
>>> "Hello world"
"""


def master_yoda(text):
    t = text.split()
    q = t[::-1]
    e = " ".join(q)
    print(e)


master_yoda('We are ready')


"""
almost_there: на входе число n, вернуть True если n находится не далее чем на 10 от чисел 100 или 200.

almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True

Замечание: abs(num) возвращает абсолютное значение числа
"""


def almost_there(n):
    if n in range(90, 111) or n in range(190, 211):
        return True
    else:
        return False
    pass


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(215))


"""
Найти 33: На входе список чисел, вернуть True если массив содержит где-нибудь 3 рядом с 3.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
"""


def has_33(nums):
    b = False
    for num in range(0, len(nums) - 1):
        if nums[num] == nums[num + 1]:
            b = True
            break
    return b


# проверка
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print(has_33([3, 1, 2, 5, 3, 3, 8, 3]))


"""
paper_doll: На входе строка, вернуть строку где каждый символ исходной строки повторяется три раза.

paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
"""


def paper_doll(text):
    a = ""
    for let in text:
        a += let * 3
    print(a)


# проверка
paper_doll('Hello')
paper_doll('Mississippi')


"""
blackjack: На входе три числа от 1 до 11. Если их сумма меньше или равна 21, 
то вернуть их сумму. Если сумма больше 21 и среди чисел есть 11, то уменьшить общую сумму на 10.
И наконец, если сумма (в том числе после уменьшения) превышает 21, вернуть 'BUST'.

blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
"""


def blackjack(a, b, c):
    if (a + b + c) <= 21:
        print(a + b + c)
    elif (a + b + c) > 21:
        if a == 11 or b == 11 or c == 11:
            if (a + b + c - 10) < 21:
                print(a + b + c - 10)
        else:
            print('BUST')


# проверка
blackjack(5, 6, 7)
blackjack(9, 9, 9)
blackjack(9, 9, 11)
