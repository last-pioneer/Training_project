"""
Быстрая сортировка слиянием.
Сложность алгоритма O(n log n).
"""


# Функция слияния двух отсортированных списков.
def merge_list(x, y):
    n = len(x)
    m = len(y)
    z = []
    i = 0
    j = 0

    while i < n and j < m:
        if x[i] < y[j]:
            z.append(x[i])
            i += 1
        else:
            z.append(y[j])
            j += 1
    z += x[i:] + y[j:]
    return z


# функция деления списка и слияния списков в общий отсортированный список
def split_and_merge(a):
    a1 = a[:len(a)//2]
    a2 = a[len(a)//2:]

    if len(a1) > 1:  # если длина 1 -го списка больше 1, то рекурсивно делим дальше.
        a1 = split_and_merge(a1)
    if len(a2) > 1:  # если длина 2 -го списка больше 1, то рекурсивно делим дальше.
        a2 = split_and_merge(a2)

    return merge_list(a1, a2)  # Слияние двух отсортированных списков в 1.


d = [7, 5, -8, -47, 50, 0, 22, - 12, 5, -30, 27, -7, 10, 1]
d = split_and_merge(d)

print(d)

