#INTRO TO IT 2nd COURSE
# Задача 11: Вернуть сумму всех элементов списка.
 
# Правильное решение:
def wrong_sum_elements(lst):
    summ = 0
    for i in lst:
        summ += i
    return summ
lst = [1,2,3,4,5]
print(wrong_sum_elements(lst))