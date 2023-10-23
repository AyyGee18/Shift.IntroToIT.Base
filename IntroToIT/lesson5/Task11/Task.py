#INTRO TO IT 2nd COURSE
# Задача 11: Вернуть сумму всех элементов списка.
 
# Исправленное решение:
def sum_elements(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total

