"""
Тренировочный файл
"""

"""
summer_69: Вернуть сумму чисел в массиве, кроме набора чисел который начинается 
с 6 и продолжается до 9 (для каждого числа 6 далее где-то будет число 9). 
Вернуть 0 если чисел нет.

summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
"""


def summer_69(arr):
    k = len(arr)
    t = 0
    s = 0
    while arr[t] != 6 and (k - 1) >= t:
        s += arr[t]
        t += 1
    while t != 9 and (k - 1) > t:
        t += 1
    while t != len(arr) and (k - 1) > t:
        s += arr[t]
    print(s)


# проверка
summer_69([1, 3, 5])
# summer_69([4, 5, 6, 7, 8, 9])
# summer_69([2, 1, 6, 9, 11])