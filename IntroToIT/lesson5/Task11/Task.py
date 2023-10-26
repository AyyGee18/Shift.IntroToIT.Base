#INTRO TO IT 2nd COURSE
# Задача 11: Вернуть сумму всех элементов списка.
 
# Неправильное решение:
def correct_sum_elements(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    print(total)
    return total

correct_sum_elements([10, 12, 23, -3])