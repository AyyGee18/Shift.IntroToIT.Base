#INTRO TO IT 2nd COURSE
# Задача 11: Вернуть сумму всех элементов списка.
 
# Решение:
def true_sum_elements(lst):
    total = 0
    for i in range(1,len(lst)):
        total += lst[i]
    return total
lst = [1,3,9]
print(true_sum_elements(lst))







