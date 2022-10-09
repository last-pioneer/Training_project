"""
Числа

Задача 1: конвертировать 1024 в двоичный и шестнадцатеричный формат
"""
q = bin(1024)
w = hex(1024)
print(q)
print(w)

"""
Задача 2: округлить 5.23222 до двух цифр после запятой
"""
e = round(5.23222, 2)
print(e)

"""
Строки

Задача 3: проверить, являются ли все буквы в строке s прописными
"""
s = 'hello how are you Mary, are you feeling okay?'
print(s.islower())


"""
Задача 4: сколько раз буква 'w' встречается в строке ниже?
"""
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))


"""
Множества

Задача 5: найдите элементы в множества set1, которых нет в множестве set2:
"""
set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}
print(set1.difference(set2))

"""
Задача 6: найдите все элементы, которые содержатся хотя бы в одном из двух множеств:
"""
set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}
print(set1.union(set2))

"""
Словари

Задача 7: создайте вот такой словарь, используя генератор словарей 
(dictionary comprehension): {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
"""
print({x: x**3 for x in range(5)})

"""
Списки
Задача 8: выполните реверсию для списка ниже:
"""
list1 = [1, 2, 3, 4]
list1.reverse()
print(list1)

"""
Задача 9: отсортируйте список ниже:
"""
list2 = [3, 4, 2, 5, 1]
list2.sort()
print(list2)
