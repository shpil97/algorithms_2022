"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""


from random import randint


def lst_min_1(lst):  # O(n ** 2)
    for i in lst:
        is_min = True
        for j in lst:
            if i > j:
                is_min = False
        if is_min:
            return i


def lst_min_2(lst):   # O(N)
    min_num = lst[0]
    for i in lst:
        if i < min_num:
            min_num = i
    return min_num


lst1 = [randint(0, 100) for i in range(20)]
print(lst1)
print(lst_min_1(lst1))
print(lst_min_2(lst1))
