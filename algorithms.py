"""
Тут будут интересные алгоритмы и красивые решения.
"""

# Рассчитываем и распечатываем ряд Фибоначи до числа n.
n = int(input())
f_1 = 0
f_2 = 1
for _ in range(n):
    f_2 = f_1 + f_2
    f_1 = f_2 - f_1
    print(f_1, end=' ')